import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from uvicorn import run

from ..auth_config import AuthConfig
from ..config import SetupConfig, read_config_file
from ..functions import FunctionStore
from ..llm import LLM
from ..runner import Runner
from ..runs import RunStore
from ..sandbox import get_sandbox_from_code_exec_mode
from ..store import ShaperStore
from .auth import router as auth_router
from .root import router as root_router
from .settings import init_settings
from .shapers import RunFailedException
from .shapers import router as shapers_router
from .state import state

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    settings = init_settings(config_path=app.state.config_path)
    print("Settings:")
    for key, value in settings.model_dump().items():
        print(f"- {key}: {value}")
    print("-" * 50)

    shaper_store_path = settings.partial_config_path / "shapers"
    function_store_path = settings.partial_config_path / "functions"
    run_store_path = settings.partial_config_path / "runs"
    auth_config_path = settings.partial_config_path / "auth.json"

    state.run_store = RunStore(path=run_store_path)
    state.shaper_store = ShaperStore(path=shaper_store_path)
    state.auth = AuthConfig(path=auth_config_path)

    setup_config = read_config_file(settings.partial_config_path / "setup.json")
    if setup_config is None:
        setup_config = SetupConfig()

    llm_instance = LLM(
        provider=setup_config.llm.value, config_path=settings.partial_config_path
    )
    sandbox = get_sandbox_from_code_exec_mode(
        setup_config.code_execution, settings.partial_config_path
    )
    function_store = FunctionStore(path=function_store_path)

    state.runner = Runner(
        llm=llm_instance,
        sandbox=sandbox,
        store=function_store,
        quiet=True,
        progress=False,
        output_file=None,
        input_schema=None,
        invalid_mode=None,
    )

    yield
    print("Shutting down")
    state.runner.terminate()


class API:
    host: str
    port: int
    config_path: str

    def __init__(
        self, host: str = "127.0.0.1", port: int = 2121, config_path: str = None
    ):
        self.host = host
        self.port = port
        self.config_path = config_path

    def _initialize_fastapi_app(self):
        app = FastAPI(lifespan=lifespan)

        # Add CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.state.config_path = self.config_path

        @app.exception_handler(RunFailedException)
        async def run_failed_exception_handler(request, exc):
            return JSONResponse(status_code=542, content=jsonable_encoder(exc.body))

        app.include_router(prefix="", router=root_router)
        app.include_router(prefix="/shapers", router=shapers_router)
        app.include_router(prefix="/auth", router=auth_router)

        return app

    def start(self):
        app = self._initialize_fastapi_app()
        run(app, host=self.host, port=self.port)
