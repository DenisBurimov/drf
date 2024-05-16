import os
from pathlib import Path

# from .base import env


BASE_DIR = Path(__file__).resolve().parent.parent.parent
# testing_env = str(
#     BASE_DIR / "testing.env"
# )  # replace with the path to your first .env file
# if os.path.exists(testing_env):
#     env.read_env(testing_env)


if os.environ.get("APP_ENV") == "testing":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
