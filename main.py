import os

import aiohttp
import firebase_admin
from fastapi import FastAPI, Depends

from v1 import http
from v1.deps import authenticate_user, get_settings
from v1.routers import health, login, contact

os.environ["TZ"] = "UTC"

settings = get_settings()

title_detail = settings.PROJECT_ID
version = settings.SHORT_SHA
api = FastAPI(title=f"Contacts API: {title_detail}", version=version)

# /
api.include_router(health.router)

# /v1
api_v1_prefix = "/v1"

# /v1/login
api.include_router(login.router, prefix=api_v1_prefix)

# /v1/contacts
api.include_router(contact.router, prefix=api_v1_prefix, tags=["contacts"], dependencies=[Depends(authenticate_user)])


@api.on_event("startup")
async def startup_event() -> None:
    firebase_admin.initialize_app()
    http.client.open(timeout=aiohttp.ClientTimeout(
        total=2 * 60,
        connect=5,
        sock_connect=5,
        sock_read=5,
    ))


@api.on_event("shutdown")
async def shutdown_event() -> None:
    await http.client.close()
