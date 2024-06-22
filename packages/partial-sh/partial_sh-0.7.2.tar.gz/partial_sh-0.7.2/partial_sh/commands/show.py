from pathlib import Path

import typer
from typing_extensions import Annotated

from ..shaper import ShaperConfigFile
from ..store import ShaperStore

app = typer.Typer()

config_path: Path = Path.home() / ".config" / "partial"
shapers_path = config_path / "shapers"


def display_shaper(name, filepath, shaper_data: ShaperConfigFile):
    print(f"Shaper: {name}\nFile: {filepath}\n-------------------")

    # Info section
    print(f"ID: {shaper_data.id}")
    print(f"Created at: {shaper_data.created_at}")
    print(f"Updated at: {shaper_data.updated_at}")
    print("")
    # Instructions section
    print("Instructions:")
    for i, instruction in enumerate(shaper_data.instructions, 1):
        print(f"  {i}. {instruction.instruction} (Mode: {instruction.mode.value})")

    # Functions section
    print("\nFunctions:")
    for name, code in shaper_data.functions.items():
        new_lines = code.replace("\n", "\n    ")
        print(f"- {name}:\n\n    {new_lines}")

    # Other details
    print(f"\nRepeat: {shaper_data.repeat}")


@app.callback(invoke_without_command=True)
def show(
    name_or_id: Annotated[
        str,
        typer.Argument(
            help="Name or ID of the shaper to show",
        ),
    ],
    json_output: Annotated[
        bool,
        typer.Option(
            "--json",
            "-j",
            help="Show the output in JSON format",
        ),
    ] = False,
):
    """
    Show the shaper content
    """
    store = ShaperStore(path=shapers_path)
    store.refresh()

    shaper = store.get_by_id(name_or_id) or store.get_by_name(name_or_id)
    if shaper is None:
        print(f"Shaper not found: {name_or_id}")
        raise typer.Exit(1)

    if json_output:
        print(shaper.json(indent=4))
        return

    if shaper.content is None:
        print(f"Shaper content not found: {name_or_id}")
        raise typer.Exit(1)

    display_shaper(shaper.name, store.path / shaper.filename, shaper.content)
