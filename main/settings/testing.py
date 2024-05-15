import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


if os.environ.get("APP_ENV") == "testing":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
