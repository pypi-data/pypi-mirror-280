import sys
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import uuid4

from langchain.pydantic_v1 import BaseModel

from .shaper import Shaper


class RunStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class InputMode(Enum):
    STDIN_ = "STDIN"
    FILE_ = "FILE"
    API = "API"


class LogItemCode(BaseModel):
    input: Any
    output: Any
    instruction: str
    code: str
    created_at: str | None


class LogItemLlm(BaseModel):
    input: Any
    output: Any
    instruction: str
    created_at: str | None


class RunFile(BaseModel):
    id: str
    shaper_id: str
    start_time: str | None = None
    end_time: str | None = None
    duration_sec: float | None = None
    status: RunStatus
    input_mode: InputMode
    created_at: str
    updated_at: str
    logs: list[dict] | None = None


class Run:
    shaper: Shaper
    id: str
    start_time: datetime | None
    end_time: datetime | None
    duration_sec: float | None
    status: RunStatus
    input_mode: InputMode
    created_at: datetime
    updated_at: datetime
    logs: list[dict] = None
    outputs: list | None = None

    def __init__(self, shaper: Shaper, input_mode: InputMode):
        self.shaper = shaper
        self.input_mode = input_mode
        self.id = str(uuid4())
        self.status = RunStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def start(self):
        self.start_time = datetime.now()
        self.status = RunStatus.RUNNING
        self.updated_at = datetime.now()
        return self

    def end(self, status: RunStatus):
        self.end_time = datetime.now()
        self.status = status
        self.updated_at = datetime.now()
        self.duration_sec = calculate_duration(self.start_time, self.end_time)
        return self

    def log(self, log_item: LogItemLlm | LogItemCode):
        if self.logs is None:
            self.logs = []
        log_item.created_at = datetime.now().isoformat()
        self.logs.append(log_item)
        self.updated_at = datetime.now()
        return self


def calculate_duration(start_time, end_time):
    if start_time and end_time:
        delta = end_time - start_time
        return round(delta.total_seconds(), 3)
    return None


def print_info(info: str, *args, **kwargs):
    """
    Print info to stderr, to avoid interfering with the output.
    """
    print(info, *args, **kwargs, file=sys.stderr)


def save_run(run: Run, run_store_path: Path, quiet: bool = False):
    run_id = run.id.split("-")[0]

    run_file_path = run_store_path / f"{run_id}.json"

    run_file = RunFile(
        id=run_id,
        shaper_id=run.shaper.id.split("-")[0],
        start_time=run.start_time.isoformat() if run.start_time else None,
        end_time=run.end_time.isoformat() if run.end_time else None,
        duration_sec=run.duration_sec,
        status=run.status.value,
        input_mode=run.input_mode.value,
        created_at=run.created_at.isoformat(),
        updated_at=run.updated_at.isoformat(),
        logs=run.logs,
    )

    # print(run_file.json(indent=4))
    with open(run_file_path, "w") as f:
        f.write(run_file.json(indent=4))

    if quiet is False:
        print_info("Run   Id:", run_id, "saved to:", run_file_path)

    return run_file
