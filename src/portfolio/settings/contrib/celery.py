import ssl

from environment import env

from ..django import TIME_ZONE as DJANGO_TIME_ZONE


CELERY_BROKER_URL = env.str("CELERY_BROKER", default="redis://redis:6379/1")

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = DJANGO_TIME_ZONE

CELERYBEAT_SCHEDULE = {}

CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True

# Celery and Redis TLS config
CELERY_BROKER_USE_SSL = {
    "ssl_cert_reqs": ssl.CERT_NONE,
}
CELERY_REDIS_BACKEND_USE_SSL = {
    "ssl_cert_reqs": ssl.CERT_NONE,
}
