import importlib
import logging
import os
import sys
from pathlib import Path
from typing import Optional

import typer
from typing_extensions import Annotated

from ..auth_config import AuthConfig
from ..cloud_service import CloudService
from ..config import CodeExecutionProvider, SetupConfig, read_config_file
from ..functions import FunctionStore
from ..input import read_input
from ..json_schema import InvalidMode
from ..llm import LLM, Modes
from ..run import InputMode, Run, save_run
from ..runner import Runner
from ..sandbox import Sandbox, SandboxMode
from ..shaper import Shaper
from ..store import ShaperStore
from .demo import run_demos
from .examples import epilog_example, help_examples
from .utils import MutuallyExclusiveGroup

APP_NAME = "partial-sh"

app = typer.Typer(no_args_is_help=True)


llm_code_exclusive_group = MutuallyExclusiveGroup()


def version_callback(value: bool):
    if value:
        pkg_name = APP_NAME.replace("-", "_")
        pkg_version = importlib.metadata.version(pkg_name)
        print(f"{pkg_name} {pkg_version}")
        raise typer.Exit()


def examples_callback(value: bool):
    if value:
        print(help_examples)
        raise typer.Exit()


def demo_callback(value: bool):
    if value:
        run_demos()
        raise typer.Exit()


def print_info(info: str, *args, **kwargs):
    """
    Print info to stderr, to avoid interfering with the output.
    """
    print(info, *args, **kwargs, file=sys.stderr)


def save_shaper(shaper: Shaper, shaper_store_path: Path, quiet: bool = False):
    slug = shaper.get_slug()
    filepath = shaper_store_path / f"{slug}.json"
    shaper.save_to_file(file=filepath)
    if quiet is False:
        short_id = shaper.id.split("-")[0]
        print_info("Shaper Id:", short_id, "saved to:", filepath)


@app.callback(invoke_without_command=True, epilog=epilog_example)
def main(
    ctx: typer.Context,
    instruction: Annotated[
        list[str],
        typer.Option(
            "--instruction",
            "-i",
            help="Instructions to follow",
            rich_help_panel="Execution",
        ),
    ] = None,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            callback=version_callback,
            is_eager=True,
            rich_help_panel="Info",
        ),
    ] = None,
    examples: Annotated[
        Optional[bool],
        typer.Option(
            "--examples",
            callback=examples_callback,
            is_eager=True,
            rich_help_panel="Info",
        ),
    ] = None,
    demo: Annotated[
        Optional[bool],
        typer.Option(
            "--demo",
            callback=demo_callback,
            is_eager=True,
            help="Run the demo",
            rich_help_panel="Info",
        ),
    ] = None,
    debug: Annotated[
        bool,
        typer.Option(
            "--debug", "-d", help="Show debug information", rich_help_panel="Execution"
        ),
    ] = False,
    regenerate: Annotated[
        bool,
        typer.Option(
            "--regenerate",
            "-R",
            help="Regenerate the code",
            rich_help_panel="Execution",
        ),
    ] = False,
    llm_mode: Annotated[
        Optional[bool],
        typer.Option(
            "--llm",
            "-l",
            help="Use LLM to execute the transformation",
            callback=llm_code_exclusive_group,
            rich_help_panel="Execution",
        ),
    ] = None,
    code_mode: Annotated[
        Optional[bool],
        typer.Option(
            "--code",
            "-c",
            help="Generate code to execute the transformation",
            callback=llm_code_exclusive_group,
            rich_help_panel="Execution",
        ),
    ] = None,
    sandbox_mode: Annotated[
        Optional[SandboxMode],
        typer.Option(
            "--sandbox",
            "-S",
            help="Use sandbox code execution",
            rich_help_panel="Execution",
            case_sensitive=False,
        ),
    ] = None,
    repeat: Annotated[
        int,
        typer.Option(
            "--repeat",
            "-r",
            help="Repeat the instruction multiple time",
            min=1,
            max=10,
            rich_help_panel="Execution",
        ),
    ] = 1,
    file: Annotated[
        Optional[Path],
        typer.Option(
            "--file",
            "-f",
            help="Read the input data from a file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
            rich_help_panel="Execution",
        ),
    ] = None,
    shaper_arg: Annotated[
        Optional[str],
        typer.Option(
            "--shaper",
            "-p",
            help="Id, Name or File of the shaper",
            rich_help_panel="Execution",
        ),
    ] = None,
    config_file: Annotated[
        Optional[Path],
        typer.Option(
            "--config",
            help="Path to the json config file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
            rich_help_panel="Execution",
        ),
    ] = None,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            "-q",
            help="Only display the output data",
            rich_help_panel="Execution",
        ),
    ] = False,
    progress: Annotated[
        bool,
        typer.Option(
            help="Display progress bar, if it's a tty and not quiet",
            rich_help_panel="Execution",
        ),
    ] = False,
    invalid_mode: Annotated[
        Optional[InvalidMode],
        typer.Option(
            "--invalid",
            help="When a json line is invalid against the schema. 'ignore' 'skip' or 'abort'",
            rich_help_panel="Execution",
            case_sensitive=False,
        ),
    ] = InvalidMode.abort.value,
    save: Annotated[
        bool,
        typer.Option(
            "--save",
            "-s",
            help="Save the shaper",
            rich_help_panel="Execution",
        ),
    ] = False,
    name: Annotated[
        Optional[str],
        typer.Option(
            "--name",
            "-n",
            help="Name of the shaper",
            rich_help_panel="Execution",
        ),
    ] = None,
    output_file: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            help="Path to the output file",
            writable=True,
            readable=False,
            resolve_path=False,
            rich_help_panel="Execution",
        ),
    ] = None,
):
    """
    Transform JSON data with LLM
    """
    # Config path
    config_path = os.getenv("PARTIAL_CONFIG_PATH", None)
    if config_path is None:
        config_path: Path = Path.home() / ".config" / "partial"
    else:
        config_path: Path = Path(config_path)

    # Define store storage paths
    function_store_path = config_path / "functions"
    shaper_store_path = config_path / "shapers"
    run_store_path = config_path / "runs"
    # Create storage folders
    config_path.mkdir(parents=True, exist_ok=True)
    function_store_path.mkdir(parents=True, exist_ok=True)
    shaper_store_path.mkdir(parents=True, exist_ok=True)
    run_store_path.mkdir(parents=True, exist_ok=True)

    if config_file is None:
        config_file = config_path / "setup.json"

    setup_config = read_config_file(config_file)

    if setup_config is None:
        config_file = None
        setup_config = SetupConfig()

    auth_config = AuthConfig(path=config_path / "auth.json").load()

    # Pass values to the context
    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug
    ctx.obj["config_path"] = config_path
    ctx.obj["auth"] = auth_config
    ctx.obj["cloud_service"] = CloudService()

    if ctx.invoked_subcommand is not None:
        return

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    if sys.stdout.isatty() is False:
        quiet = True

    if quiet is False:
        # Display config
        print_info("LLM:", setup_config.llm.value)

    # Check the code execution provider from config file if no flags
    if sandbox_mode is None:
        if setup_config.code_execution == CodeExecutionProvider.E2B:
            sandbox_mode = SandboxMode.E2B
        elif setup_config.code_execution == CodeExecutionProvider.DOCKER:
            sandbox_mode = SandboxMode.DOCKER
        elif setup_config.code_execution == CodeExecutionProvider.LOCAL:
            sandbox_mode = SandboxMode.NO
        elif setup_config.code_execution not in list[CodeExecutionProvider]:
            typer.echo("Invalid code execution provider", err=True)
            raise typer.Exit(1)

    # If NO run in local
    if sandbox_mode == SandboxMode.NO:
        sandbox_mode = None

    if quiet is False:
        # Display only the current parameters that will be use for this run
        if sandbox_mode is not None:
            print_info(f"Code execution: sandbox ({sandbox_mode.value})")
        else:
            print_info("Code execution: local")

    llm_instance = LLM(provider="openai", config_path=config_path)

    sandbox = (
        Sandbox(provider=sandbox_mode, config_path=config_path)
        if sandbox_mode
        else None
    )

    function_store = FunctionStore(path=function_store_path)
    function_store.refresh()

    lines = read_input(file=file) if file else read_input()

    shaper = Shaper()

    # Check if shaper arg is a file
    shaper_store = ShaperStore(path=shaper_store_path)
    if shaper_arg:
        shaper_file = shaper_store.find_shaper_file(shaper_arg)

        if not shaper_file:
            typer.echo(f"Shaper not found: {shaper_arg}", err=True)
            raise typer.Exit(1)

        shaper = shaper.load_from_file(shaper_file)
    else:
        if llm_mode:
            mode = Modes.LLM
        elif code_mode:
            mode = Modes.CODE
        else:
            mode = None

        shaper = shaper.new(
            name=name,
            instructions=instruction,
            repeat=repeat,
            regenerate=regenerate,
            mode=mode,
        )

    if shaper.name is None:
        shaper.name = shaper.get_prep_name()

    runner = Runner(
        llm=llm_instance,
        sandbox=sandbox,
        store=function_store,
        quiet=quiet,
        progress=progress,
        output_file=output_file,
        input_schema=shaper.input_schema,
        invalid_mode=invalid_mode,
    )

    run = Run(
        shaper=shaper,
        input_mode=InputMode.FILE_ if file else InputMode.STDIN_,
    )

    if quiet is False:
        print_info("--- start")

    run_res = runner.process(
        lines=lines,
        run=run,
    )

    runner.terminate()

    if quiet is False:
        print_info("--- end")
    # Save shaper
    if save:
        save_run(run_res, run_store_path, quiet=quiet)
        save_shaper(shaper, shaper_store_path, quiet=quiet)
