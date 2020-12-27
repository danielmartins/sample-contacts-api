import aiohttp


class AsyncHttpClient:
    session = None

    def open(self, **kwargs) -> None:  # type: ignore
        self.session = aiohttp.ClientSession(**kwargs)

    async def close(self) -> None:
        assert self.session is not None
        await self.session.close()
        self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None
        return self.session


client = AsyncHttpClient()
