from pydantic import BaseModel, EmailStr


class SignIn(BaseModel):
    email: EmailStr
    password: str


class SignInResponse(BaseModel):
    token: str
    refresh_token: str
    expires_in: int
