import traceback
from pathlib import Path

import typer
from oddrn_generator import FilesystemGenerator

from odd_cli.client import Client
from odd_cli.logger import logger
from odd_cli.reader.reader import read


def collect(
    folder: Path = typer.Argument(..., exists=True, resolve_path=True),
    platform_host: str = typer.Option(..., "--host", "-h", envvar="ODD_PLATFORM_HOST"),
    platform_token: str = typer.Option(
        ..., "--token", "-t", envvar="ODD_PLATFORM_TOKEN"
    ),
):
    """Collect and ingest metadata for local files from folder"""

    client = Client(host=platform_host, token=platform_token)

    generator = FilesystemGenerator(host_settings="local")
    try:
        client.create_data_source(
            data_source_oddrn=generator.get_data_source_oddrn(),
            data_source_name="local_files",
        )

        data_entities = read(path=folder, generator=generator)

        client.ingest_data_entity_list(data_entities=data_entities)

        logger.success(f"Ingested {len(data_entities.items)} datasets")
    except Exception as e:
        logger.debug(traceback.format_exc())
        logger.error(e)
        raise typer.Exit(code=1)
