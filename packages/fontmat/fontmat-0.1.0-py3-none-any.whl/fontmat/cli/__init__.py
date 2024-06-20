from pathlib import Path

import click
from fontTools import ttLib

from fontmat import __version__
from fontmat.cli.constants import METADATA


@click.command()
@click.argument(
    "font_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
@click.version_option(version=__version__)
def main(font_path: Path) -> None:
    """A CLI to check font metadata."""
    with ttLib.TTFont(font_path) as f:
        for metadatum in METADATA:
            value = f["name"].getDebugName(metadatum["name_id"])
            value_display = "-" if value is None else value

            click.echo(f"{metadatum['label']}: {value_display}")
