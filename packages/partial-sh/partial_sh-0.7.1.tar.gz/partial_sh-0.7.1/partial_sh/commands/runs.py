from datetime import datetime
from pathlib import Path
from typing import Annotated

import typer
from tabulate import tabulate

from ..runs import RunInfo, RunsOutput, RunStore

app = typer.Typer()


def parse_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return None


def format_datetime(date_obj):
    if date_obj:
        return date_obj.strftime("%Y-%m-%d %H:%M:%S")
    return "N/A"


def calculate_duration(start_time, end_time):
    if start_time and end_time:
        delta = end_time - start_time
        return round(delta.total_seconds(), 3)
    return "N/A"


def display_runs(runs_output: RunsOutput, full_path: bool = False):
    runs_path = runs_output.location
    headers = [
        "RUN ID",
        "SHAPER ID",
        "START TIME",
        "END TIME",
        "DURATION (s)",
        "STATUS",
        "INPUT MODE",
        "CREATED AT",
        "UPDATED AT",
    ]
    if full_path:
        headers.append("FILE")
    table = []

    for run_id, run_info in runs_output.runs.items():
        start_time = parse_datetime(run_info.start_time)
        end_time = parse_datetime(run_info.end_time)

        row = [
            run_id,
            run_info.shaper_id,
            format_datetime(start_time),
            format_datetime(end_time),
            run_info.duration_sec
            if run_info.duration_sec
            else calculate_duration(start_time, end_time),
            run_info.status,
            run_info.input_mode,
            format_datetime(parse_datetime(run_info.created_at)),
            format_datetime(parse_datetime(run_info.updated_at)),
        ]
        if full_path:
            row.append(runs_path / f"{run_id}.json")
        table.append(row)

    table = sorted(table, key=lambda x: x[7], reverse=True)

    print(f"Location: {runs_path}\n")
    print(tabulate(table, headers=headers, tablefmt="simple"))


def prepare_runs_data(runs_path: Path, run_infos: list[RunInfo]):
    runs_output = RunsOutput(location=runs_path)
    for run_info in run_infos:
        runs_output.runs[run_info.id] = run_info
    return runs_output


@app.callback(invoke_without_command=True)
def list_runs(
    ctx: typer.Context,
    json_output: Annotated[
        bool,
        typer.Option(
            "--json",
            "-j",
            help="Show the output in JSON format",
        ),
    ] = False,
    full_path: Annotated[
        bool,
        typer.Option("--full-path", "-f", help="Show the full file path."),
    ] = False,
):
    """
    List the runs in the store.
    """
    config_path = Path(ctx.obj["config_path"])
    runs_path = config_path / "runs"

    run_store = RunStore(runs_path)
    run_store.refresh()

    runs_output = prepare_runs_data(run_store.path, run_store.run_infos)

    if json_output:
        print(runs_output.json(indent=4))
    else:
        display_runs(runs_output, full_path=full_path)
