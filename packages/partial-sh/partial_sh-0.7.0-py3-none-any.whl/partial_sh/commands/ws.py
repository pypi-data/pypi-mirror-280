import json
from pathlib import Path

import requests
import typer

from . import auth

app = typer.Typer()


def get_workspace_id_by_name(workspaces, default):
    for workspace in workspaces["workspaces"]:
        if workspace["name"] == default:
            return workspace["id"]
    return None


def add_default_workspace_to_setup_file(default_ws_id, config_path):
    setup_file = config_path / "setup.json"
    with open(setup_file, "r") as f:
        setup = json.load(f)
    setup["default_workspace"] = default_ws_id
    with open(setup_file, "w") as f:
        json.dump(setup, f, indent=4)


def extract_default_workspace_id(config_path):
    setup_file = config_path / "setup.json"
    with open(setup_file, "r") as f:
        setup = json.load(f)
    return setup.get("default_workspace", None)


@app.callback(invoke_without_command=True)
def list_workspaces(
    ctx: typer.Context,
    default: str = typer.Option(
        None,
        "--default",
        "-d",
        help="Set the default workspace",
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        "-j",
        help="Show the output in JSON format",
    ),
):
    """
    List all the available workspaces.
    """

    access_token = auth.get_access_token(ctx)
    cloud_service = ctx.obj["cloud_service"]
    try:
        workspaces = cloud_service.list_workspaces(access_token)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        if e.response.status_code == 401:
            print("Unauthorized. Please login again.")
        raise typer.Abort()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        raise typer.Abort()

    if default:
        default_ws_id = get_workspace_id_by_name(workspaces, default)
        if default_ws_id is None:
            print("Default workspace not found.")
        else:
            config_path = Path(ctx.obj["config_path"])
            add_default_workspace_to_setup_file(default_ws_id, config_path)
            print("Default workspace ID:", default_ws_id)
    else:
        default_ws_id = extract_default_workspace_id(Path(ctx.obj["config_path"]))

    # Display workspaces
    if json_output:
        print(json.dumps(workspaces, indent=4))
    else:
        for workspace in workspaces["workspaces"]:
            default_suffix = "(default)" if workspace["id"] == default_ws_id else ""
            print("Workspace:", default_suffix)
            for key, value in workspace.items():
                print(f"{key}: {value}")
            print("\n")
