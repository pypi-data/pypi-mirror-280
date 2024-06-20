import logging
import socket
from pathlib import Path
from random import randint

import typer

from ..api.main import API

app = typer.Typer()


def find_available_port(port: int):
    if port < 1024 or port > 65535:
        raise ValueError("Port number must be between 1024 and 65535")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        res = s.connect_ex(("localhost", port))
    if res == 0:
        return find_available_port(port + 1)
    return port


def display_login_prompt(webapp_url, randomCode):
    print("--------------------------------------------------")
    print()
    print("      CLI Login to Partial.sh")
    print()
    print("1. Visit the URL to login:")
    print("   " + webapp_url)
    print()
    print("2. Enter the Confirmation Code:")
    print("   " + str(randomCode))
    print()
    print("Waiting for confirmation...")
    print()
    print("--------------------------------------------------")


@app.callback(invoke_without_command=True)
def login(
    ctx: typer.Context,
    host: str = typer.Option("127.0.0.1", help="Host to listen on"),
    port: int = typer.Option(2121, help="Port to listen on"),
):
    """Login to the application."""

    port = find_available_port(port)

    randomCode = randint(1000, 9999)
    webapp_base = ctx.obj["cloud_service"].webapp_url
    webapp_url = (
        f"{webapp_base}/auth/authorize?listenPort={port}&confirmCode={randomCode}"
    )

    display_login_prompt(webapp_url, randomCode)

    config_path = Path(ctx.obj["config_path"])

    api = API(host=host, port=port, config_path=config_path)

    # Disable logging to not pollute the output while login
    logging.disable(logging.CRITICAL)

    api.start()
