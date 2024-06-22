from pathlib import Path

import typer

from ..api.main import API

app = typer.Typer()


@app.callback(invoke_without_command=True)
def serve(
    ctx: typer.Context,
    host: str = typer.Option("127.0.0.1", help="Host to serve on"),
    port: int = typer.Option(2121, help="Port to serve on"),
):
    print("Starting the API server...")

    config_path = Path(ctx.obj["config_path"])

    api = API(host=host, port=port, config_path=config_path)

    api.start()
