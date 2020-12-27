from functools import lru_cache

from v1 import settings


@lru_cache()
def get_settings():
    return settings.Settings()

