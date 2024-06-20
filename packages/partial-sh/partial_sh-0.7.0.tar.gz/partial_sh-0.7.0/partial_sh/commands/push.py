import json
from datetime import datetime
from pathlib import Path

import requests
import typer
from pydantic import BaseModel
from typing_extensions import Annotated

from ..shaper import prepare_key
from ..store import ShaperInfo, ShaperStore
from . import auth
from .ws import extract_default_workspace_id, get_workspace_id_by_name

app = typer.Typer()


class ResponseModel(BaseModel):
    id: str
    name: str
    content: dict
    created_at: datetime
    updated_at: datetime


def get_store(config_path: Path):
    """Retrieves shaper data from the given configuration path."""
    shapers_path = config_path / "shapers"
    store = ShaperStore(path=shapers_path)

    try:
        store.refresh()
    except Exception as e:
        print(f"Error refreshing the shaper store: {e}")
        raise typer.Exit(code=1)
    return store


@app.callback(invoke_without_command=True)
def push(
    ctx: typer.Context,
    workspace: Annotated[
        str, typer.Option("--workspace", "-w", help="Workspace to push the shaper to.")
    ] = None,
    name_id: str = typer.Argument(..., help="Name or ID of the shaper"),
):
    """
    Push a new shaper to the store.
    """

    config_path = Path(ctx.obj["config_path"])
    access_token = auth.get_access_token(ctx)
    cloud_service = ctx.obj["cloud_service"]

    if workspace is None:
        workspace = extract_default_workspace_id(config_path)
        if workspace is None:
            print("No workspace specified. Use --workspace or set a default workspace.")
            raise typer.Exit(code=1)

    if workspace.startswith("wks_"):
        workspace_id = workspace
    else:
        # search workspace by name
        workspaces = cloud_service.list_workspaces(access_token)
        if workspaces is None:
            print("No workspaces found.")
            raise typer.Exit(code=1)
        workspace_id = get_workspace_id_by_name(workspaces, workspace)

    store = get_store(config_path)

    # Check by name first
    name = prepare_key(name_id)
    shaper_info = store.get_by_name(name)

    if shaper_info is None:
        shaper_info = store.get_by_id(name_id)
    if shaper_info is None:
        print(f"Shaper with ID {name_id} not found.")
        raise typer.Exit(code=1)

    shaper_data = json.loads(shaper_info.content.json())

    try:
        res = cloud_service.create_sahper(access_token, workspace_id, shaper_data)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        if e.response.status_code == 401:
            print("Unauthorized. Please login again.")
        raise typer.Exit(code=1)

    response = ResponseModel(**res)

    print("Pushed successfully:")
    print("-------------------")
    print("ID:  ", response.id)
    print("Name:", response.name)
    print()

    # Display Shaper URL
    print("Shaper URL:")
    print("-----------")
    print(f"{cloud_service.webapp_url}/workspaces/{workspace_id}/shapers/{response.id}")
    print()

    # Display curl command
    print("Curl Command:")
    print("-------------")
    print(
        f"""
curl -X POST '{cloud_service.api_url}/api/v1/shapers/{response.id}/run' \\
     -H "Content-Type: application/json" \\
     -H "X-API-KEY: $PARTIAL_API_KEY" \\
     --data '{{"data": [ <YOUR DATA HERE> ]}}'
    """
    )
