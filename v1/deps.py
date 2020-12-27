from functools import lru_cache

from fastapi import Security, Depends, HTTPException
from fastapi.security import APIKeyHeader, APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN

from v1 import settings
from v1.schemas.user import User
from v1.services.auth import AuthService
from v1.services.item import ContactService


@lru_cache()
def get_settings():
    return settings.Settings()


def get_contacts_service():
    return ContactService()


def get_auth_service():
    return AuthService()


API_KEY_NAME = "Authorization"

API_KEY_HEADER = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
API_KEY_QUERY = APIKeyQuery(name=API_KEY_NAME, auto_error=False)


def authenticate_user(
    api_key_query: str = Security(API_KEY_QUERY),
    api_key_header: str = Security(API_KEY_HEADER),
    auth_service: AuthService = Depends(get_auth_service)
):
    tokens = [api_key_query, api_key_header]
    for t in tokens:
        try:
            payload = auth_service.verify_id_token(t)
            return User(
                email=payload["firebase"]["identities"]["email"][0],
                uid=payload["uid"],
                user_id=payload["user_id"],
                sign_in_provider=payload["firebase"]["sign_in_provider"],
                email_verified=payload["email_verified"]
            )
        except Exception:
            continue

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )
