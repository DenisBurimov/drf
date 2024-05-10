from pathlib import Path

from environment import env

BASE_DIR = Path(__file__).resolve().parent.parent

def rel(*path):
    return BASE_DIR.joinpath(*path)

DEBUG = False

INTERNAL_IPS = env.list("INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("SECRET_KEY")

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "django_extensions",
    "django_browser_reload",
    "rest_framework",
    # our apps
    "users",
    "articles",
    "tailwind",
    "theme",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("apps/core/templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DATABASE_NAME", default="db"),
        "HOST": env.str("DATABASE_HOST", default="127.0.0.1"),
        "PORT": env.int("DATABASE_PORT", default=5432),
        "USER": env.str("DATABASE_USER", default="postgres"),
        "PASSWORD": env.str("DATABASE_PASSWORD", default="db"),
    }
}

AUTHENTICATION_BACKENDS = (
    "users.backends.UserModelBackend",
)

AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = env.str("STATIC_URL", default="/s/")
STATIC_ROOT = env.str("STATIC_ROOT", default=rel("..", "..", "public", "static"))

MEDIA_URL = env.str("MEDIA_URL", default="/m/")
MEDIA_ROOT = env.str("MEDIA_ROOT", rel("..", "..", "public", "media"))

APPEND_SLASH = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {message} {pathname}",
            "style": "{",
            "datefmt": "[%X]",
        },
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "rich_tracebacks": True,
            "formatter": "verbose",
            "level": "INFO",
        },
    },
    "loggers": {
        "": {  # 'catch all' loggers by referencing it with the empty string
            "handlers": ["console"],
            "level": "INFO",
        },
        "django": {  # 'catch all' loggers by referencing it with the empty string
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 300,
        "LOCATION": f'rediss://{env.str("REDIS_URL", default="redis:6379/2")}',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

TAILWIND_APP_NAME = "theme"
