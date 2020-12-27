from typing import Optional

import aiohttp as aiohttp

from v1.schemas.login import SignIn, SignInResponse


class AuthService:
    BASE_URL = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

    async def sign_in(self, session: aiohttp.ClientSession, sign_in: SignIn, settings) -> Optional[SignInResponse]:
        body = {"email": sign_in.email, "password": sign_in.password, "returnSecureToken": True}
        async with session.request(method="POST", url=self.BASE_URL, params={"key": settings.FIREB_API_KEY},
                                   json=body) as response:
            if response.status == 200:
                response = await response.json()
                return SignInResponse(token=response["idToken"], refresh_token=response["refreshToken"],
                                      expires_in=response["expiresIn"])
