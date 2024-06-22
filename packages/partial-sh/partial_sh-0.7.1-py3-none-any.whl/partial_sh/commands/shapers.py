from collections import defaultdict
from pathlib import Path

import typer
from langchain.pydantic_v1 import BaseModel
from tabulate import tabulate
from typing_extensions import Annotated

from ..store import ShaperInfo, ShaperStore

app = typer.Typer()


class ShapersOutput(BaseModel):
    """Represents the output structure for shapers."""

    location: Path
    shapers: list[ShaperInfo]


def display_shapers(
    shapers_output: ShapersOutput, all_: bool = True, full_path: bool = False
):
    """Displays the shaper information in a formatted table.

    Args:
        shapers_output (ShapersOutput): The output object containing shaper information.
        all_ (bool): If True, display all shapers. If False, display only the latest shaper for each name.
    """
    if not shapers_output.shapers:
        print("Location:", shapers_output.location)
        print("No shapers to display.")
        return

    headers = ["SHAPER NAME", "ID", "FILENAME", "LAST UPDATED"]
    table = []

    # Group shapers by name
    shapers_by_name = defaultdict(list)
    for shaper in shapers_output.shapers:
        shapers_by_name[shaper.name].append(shaper)

    for name, shapers in shapers_by_name.items():
        shapers = sorted(shapers, key=lambda x: x.updated_at, reverse=True)
        for i, shaper in enumerate(shapers):
            if i == 0 or all_:
                updated_at_str = (
                    shaper.updated_at.strftime("%Y-%m-%d %H:%M:%S")
                    if shaper.updated_at
                    else "N/A"
                )
                filename = (
                    shaper.filename
                    if not full_path
                    else shapers_output.location / shaper.filename
                )
                row = [name if i == 0 else "", shaper.id, filename, updated_at_str]
                table.append(row)

    print("Location:", shapers_output.location, "\n")
    print(tabulate(table, headers=headers, tablefmt="simple"))


def retrieve_shapers_data(config_path: Path) -> ShapersOutput:
    """Retrieves shaper data from the given configuration path."""
    shapers_path = config_path / "shapers"
    store = ShaperStore(path=shapers_path)

    try:
        store.refresh()
    except Exception as e:
        print(f"Error refreshing the shaper store: {e}")
        return ShapersOutput(location=shapers_path, shapers=[])

    return ShapersOutput(location=store.path, shapers=store.shaper_infos)


@app.callback(invoke_without_command=True)
def list_shapers(
    ctx: typer.Context,
    json_output: Annotated[
        bool,
        typer.Option(
            "--json",
            "-j",
            help="Show the output in JSON format",
        ),
    ] = False,
    all_: Annotated[
        bool,
        typer.Option(
            "--all",
            "-a",
            help="Show all shapers, not just the latest shaper for each name",
        ),
    ] = False,
    full_path: Annotated[
        bool,
        typer.Option("--full-path", "-f", help="Show the full path."),
    ] = False,
):
    """
    List all the available shapers.
    """
    config_path = Path(ctx.obj["config_path"])
    shapers_output = retrieve_shapers_data(config_path)

    if json_output:
        print(shapers_output.json(indent=4))
    else:
        display_shapers(shapers_output, all_, full_path)
