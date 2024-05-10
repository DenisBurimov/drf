from portfolio.settings import *  # noqa: W0401, W0611


SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SECRET_KEY = "fake"  # nosec

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

CONSTANCE_BACKEND = "constance.backends.memory.MemoryBackend"
