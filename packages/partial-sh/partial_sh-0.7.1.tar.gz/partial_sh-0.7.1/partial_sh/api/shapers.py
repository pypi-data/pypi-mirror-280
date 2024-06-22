from datetime import datetime
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..run import InputMode, Run, RunStatus, save_run
from ..runs import RunInfo
from ..shaper import Shaper
from ..store import ShaperInfo
from .state import state

router = APIRouter()


class SimpleShaperInfo(BaseModel):
    id: str
    name: str | None
    filename: str
    created_at: datetime
    updated_at: datetime


class ResponseShapers(BaseModel):
    shapers: list[SimpleShaperInfo]


@router.get("", description="List of shapers")
def read_shapers() -> ResponseShapers:
    shaper_store = state.shaper_store
    shaper_infos = shaper_store.list()
    simple_shaper_infos = [
        SimpleShaperInfo(**shaper.dict()) for shaper in shaper_infos if shaper is not None
    ]
    return ResponseShapers(shapers=simple_shaper_infos)


class ResponseShaper(BaseModel):
    shaper: ShaperInfo


@router.get("/{shaper_id}")
def read_shaper(shaper_id: str):
    shaper_store = state.shaper_store
    shaper_store.refresh()
    shaper_info = shaper_store.get_by_id(shaper_id)
    if shaper_info is None:
        raise HTTPException(status_code=404, detail="Shaper not found")
    # TODO: Use ResponseShape, Problem with multiple version of pydantic
    return {"shaper": shaper_info}


class RequsetRun(BaseModel):
    data: list | dict


class ResponseRun(BaseModel):
    run_id: str
    run_status: RunStatus
    outputs: list | dict


class ResponseRunFailed(BaseModel):
    run_id: str
    run_status: Literal[RunStatus.FAILED]
    error: str
    outputs: list | dict | None


class RunFailedException(Exception):
    def __init__(self, body: ResponseRunFailed):
        self.body = body


@router.post(
    "/{shaper_id}/run",
    responses={542: {"model": ResponseRunFailed, "description": "Run failed"}},
)
def shaper_data(shaper_id: str, body: RequsetRun) -> ResponseRun:
    shaper_store = state.shaper_store
    shaper_store.refresh()
    shaper_info = shaper_store.get_by_id(shaper_id)
    if shaper_info is None:
        raise HTTPException(status_code=404, detail="Shaper not found")

    shaper = Shaper().load(shaper_info.content)
    runner = state.runner
    runner.store.refresh()

    run = Run(shaper=shaper, input_mode=InputMode.API)

    data = body.data
    if isinstance(data, dict):
        data = [data]

    run_res = runner.process(lines=data, run=run, return_outputs=True)

    save_run(run_res, state.run_store.path, quiet=True)

    if run_res.outputs is not None and len(run_res.outputs) == 1:
        outputs = run_res.outputs[0]
    else:
        outputs = run_res.outputs

    if run_res.status == RunStatus.FAILED:
        response = ResponseRunFailed(
            run_id=run_res.id,
            run_status=run_res.status,
            error="Run failed",
            outputs=outputs,
        )
        raise RunFailedException(body=response)

    return ResponseRun(run_id=run_res.id, run_status=run_res.status, outputs=outputs)


class ResponseRuns(BaseModel):
    runs: list[RunInfo]


@router.get("/{shaper_id}/runs", description="List of runs for a shaper")
def read_runs(shaper_id: str) -> ResponseRuns:
    state.shaper_store.refresh()
    shaper_info = state.shaper_store.get_by_id(shaper_id)
    if shaper_info is None:
        raise HTTPException(status_code=404, detail="Shaper not found")

    runs = state.run_store.list()
    shaper_runs = [run for run in runs if run.shaper_id == shaper_id]
    # sort by most recent created first
    shaper_runs.sort(key=lambda x: x.created_at, reverse=True)
    return ResponseRuns(runs=shaper_runs)
