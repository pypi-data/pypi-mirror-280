from ..auth_config import AuthConfig
from ..runner import Runner
from ..runs import RunStore
from ..store import ShaperStore


class State:
    run_store: RunStore
    shaper_store: ShaperStore
    runner: Runner
    auth: AuthConfig


state = State()
