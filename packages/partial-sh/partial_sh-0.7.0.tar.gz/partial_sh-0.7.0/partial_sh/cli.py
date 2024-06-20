import logging

from .commands.config import app as config_app
from .commands.functions import app as functions_app
from .commands.login import app as login_app
from .commands.main import app as main_app
from .commands.push import app as push_app
from .commands.runs import app as runs_app
from .commands.server import app as server_app
from .commands.setup import app as setup_app
from .commands.shapers import app as shapers_app
from .commands.show import app as show_app
from .commands.ws import app as ws_app

main_app.add_typer(setup_app, name="setup", no_args_is_help=False, help="Setup partial")
main_app.add_typer(config_app, name="config", no_args_is_help=False, help="Config")
main_app.add_typer(
    functions_app, name="functions", no_args_is_help=False, help="Functions"
)
main_app.add_typer(shapers_app, name="shapers", no_args_is_help=False, help="Shapers")
main_app.add_typer(
    show_app, name="show", no_args_is_help=True, help="Show the content of a shaper"
)
main_app.add_typer(runs_app, name="runs", no_args_is_help=False, help="Runs")
main_app.add_typer(
    server_app, name="server", no_args_is_help=False, help="Start the API server"
)
main_app.add_typer(
    login_app, name="login", no_args_is_help=False, help="Login to the application"
)
main_app.add_typer(
    ws_app,
    name="ws",
    no_args_is_help=False,
    help="List all the available workspaces",
    rich_help_panel="Cloud",
)
main_app.add_typer(
    push_app,
    name="push",
    no_args_is_help=False,
    help="Push a shaper to the cloud store",
    rich_help_panel="Cloud",
)


def main():
    main_app()


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()
