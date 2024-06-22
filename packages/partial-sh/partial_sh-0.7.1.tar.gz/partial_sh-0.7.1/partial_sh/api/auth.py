import asyncio
import base64
import json
import os
import signal
from time import sleep

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from .state import state

router = APIRouter()


class CLIAuthResponse(BaseModel):
    status: str
    message: str = None


def stop_listenning():
    os.kill(os.getpid(), signal.SIGINT)


@router.get("/cli")
async def auth_cli(tokens: str = Query(...)) -> CLIAuthResponse:
    try:
        decoded_tokens = base64.b64decode(tokens).decode("utf-8")
        auth_config = json.loads(decoded_tokens)
        state.auth.set_auth(auth_config)

        print()
        print("+----------------------------+")
        print("| Successfully authenticated |")
        print("+----------------------------+")
        print()

        return CLIAuthResponse(
            status="authenticated", message="Successfully authenticated"
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Invalid Base64 token")
    finally:
        stop_listenning()


@router.get("/cancel")
async def auth_cancel() -> CLIAuthResponse:
    print()
    print("+-------------------------+")
    print("| Canceled authentication |")
    print("+-------------------------+")
    print()

    try:
        return CLIAuthResponse(status="canceled", message="Operation canceled")
    finally:
        stop_listenning()
