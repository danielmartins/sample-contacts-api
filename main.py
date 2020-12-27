import os

import aiohttp
from fastapi import FastAPI

from v1 import http
from v1.routers import health, item, login

os.environ["TZ"] = "UTC"

title_detail = os.getenv("PROJECT_ID", "Local")
version = os.getenv("SHORT_SHA", "local")
api = FastAPI(title=f"Contacts API: {title_detail}", version=version)

# /
api.include_router(health.router)

# /v1
api_v1_prefix = "/v1"
api.include_router(item.router, prefix=api_v1_prefix)
api.include_router(login.router, prefix=api_v1_prefix)


@api.on_event("startup")
async def startup_event() -> None:
    http.client.open(timeout=aiohttp.ClientTimeout(
        total=2 * 60,
        connect=5,
        sock_connect=5,
        sock_read=5,
    ))


@api.on_event("shutdown")
async def shutdown_event() -> None:
    await http.client.close()
