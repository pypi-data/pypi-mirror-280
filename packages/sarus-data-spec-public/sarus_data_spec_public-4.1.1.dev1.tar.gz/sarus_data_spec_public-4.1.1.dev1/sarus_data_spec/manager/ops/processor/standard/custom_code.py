from __future__ import annotations

import typing as t

import pyarrow as pa

import tempfile
from sarus_data_spec.arrow.schema import type_from_arrow_schema
from sarus_data_spec.dataset import Dataset
from sarus_data_spec.manager.async_utils import async_iter
import os
from sarus_data_spec.manager.ops.processor.standard.standard_op import parent
from sarus_data_spec.schema import schema as schema_builder
import sarus_data_spec.protobuf as sp
import sarus_data_spec.typing as st

from sarus_data_spec.manager.ops.processor.standard.standard_op import (  # noqa: E501
    StandardDatasetImplementation,
    StandardDatasetStaticChecker,
)

try:
    import docker
except ModuleNotFoundError:
    pass  # error message in typing.py


class CustomCodeStaticChecker(StandardDatasetStaticChecker):
    async def schema(self) -> st.Schema:
        """Computes the schema of the dataspec.

        The schema is computed by computing the synthetic data value and
        converting the Pyarrow schema to a Sarus schema.q
        """
        syn_variant = self.dataset.variant(kind=st.ConstraintKind.SYNTHETIC)
        assert syn_variant is not None
        assert syn_variant.prototype() == sp.Dataset

        syn_dataset = t.cast(st.Dataset, syn_variant)
        arrow_iterator = await compute_custom_code_to_arrow(
            syn_dataset, batch_size=1000
        )
        first_batch = await arrow_iterator.__anext__()
        schema = first_batch.schema

        schema_type = type_from_arrow_schema(schema)

        return schema_builder(
            self.dataset, schema_type=schema_type, properties={}
        )


class CustomCode(StandardDatasetImplementation):
    """Computes schema and arrow
    batches for a dataspec transformed by
    an push sql transform. It is used to push the data of the parents in a
    sql database.
    """

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        return await compute_custom_code_to_arrow(
            self.dataset, batch_size=batch_size
        )

    async def sql_implementation(
        self,
    ) -> t.Optional[t.Dict[t.Tuple[str, ...], str]]:
        """pass query to parents"""
        raise NotImplementedError


async def compute_custom_code_to_arrow(
    dataset: st.Dataset, batch_size: int
) -> t.AsyncIterator[pa.RecordBatch]:
    transform = dataset.transform()
    spec_custom_code = transform.protobuf().spec.custom_code
    image_name = spec_custom_code.image_name

    parent_ds = parent(dataset, kind="dataset")
    assert isinstance(parent_ds, Dataset)

    result = await parent_ds.async_to(t.AsyncIterator[pa.RecordBatch])
    batches_async_iterator = t.cast(t.AsyncIterator[pa.RecordBatch], result)

    arrow_batches = [batch async for batch in batches_async_iterator]
    input_table = pa.Table.from_batches(arrow_batches)

    table = execute_custom_code(input_table, image_name)

    return async_iter(table.to_batches(max_chunksize=batch_size))


def execute_custom_code(input_table: pa.Table, image_name: str) -> pa.Table:
    IN_DOCKER_VOLUMES_PATH = "/data/container"
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_file_name = os.path.join(tmpdirname, "input.parquet")
        output_file_name = os.path.join(tmpdirname, "output.parquet")

        # Write the Arrow Table to a Parquet file
        pa.parquet.write_table(input_table, input_file_name)

        # Initialize Docker client
        client = docker.from_env()

        _ = client.containers.run(
            image=image_name,
            volumes={
                tmpdirname: {"bind": IN_DOCKER_VOLUMES_PATH, "mode": "rw"},
            },
            environment=[
                f"INPUT_DIR={IN_DOCKER_VOLUMES_PATH}",
                f"OUTPUT_DIR={IN_DOCKER_VOLUMES_PATH}",
            ],
            detach=False,
        )

        if not os.path.exists(output_file_name):
            raise ValueError(
                "The arbitrary code does not return any output file. Please look at the documentation to build a correct image for custom code. The Docker image should return an output file named output.csv."
            )

        output_table = pa.parquet.read_table(output_file_name)
    return output_table
