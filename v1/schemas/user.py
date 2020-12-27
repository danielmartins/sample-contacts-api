from pydantic import EmailStr
from pydantic.main import BaseModel


class User(BaseModel):
    uid: str
    user_id: str
    email: EmailStr
    sign_in_provider: str
    email_verified: bool
