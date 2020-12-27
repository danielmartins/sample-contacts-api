import aiohttp
from fastapi import APIRouter, Depends, HTTPException

from v1 import http
from v1.deps import get_settings
from v1.schemas.login import SignInRequest, SignInResponse
from v1.services.auth import AuthService
from v1.settings import Settings

router = APIRouter()

auth_service = AuthService()


@router.post("/login", response_model=SignInResponse, tags=["login"])
async def login(sign_in: SignInRequest, http_client: aiohttp.ClientSession = Depends(http.client),
                settings: Settings = Depends(get_settings)):
    """
    login in google auth
    """
    token_data = await auth_service.sign_in(http_client, sign_in, settings)
    if not token_data:
        raise HTTPException(status_code=400, detail="Cant log in")

    return token_data
