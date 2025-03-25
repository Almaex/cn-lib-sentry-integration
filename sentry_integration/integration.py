import sentry_sdk
from fastapi import FastAPI
from typing import Optional

def init_sentry(
    app: FastAPI,
    dsn: str,
    environment: str,
    repository: Optional[str] = None,
    release: Optional[str] = None,
    traces_sample_rate: float = 1.0,
    send_default_pii: bool = True,
):
    tags = {}
    if repository:
        tags["repository"] = repository

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        send_default_pii=send_default_pii,
        traces_sample_rate=traces_sample_rate,
        release=release,
        tags=tags,
    )
