from portfolio.settings import *  # noqa: W0401, W0611


DEBUG = True

SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

INSTALLED_APPS = INSTALLED_APPS + [  # noqa: W0401
    "debug_toolbar",
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

DEBUG_TOOLBAR_PANELS = [
    # "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    # "debug_toolbar.panels.settings.SettingsPanel",
    # "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    # "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    # "debug_toolbar.panels.cache.CachePanel",
    # "debug_toolbar.panels.signals.SignalsPanel",
    # "debug_toolbar.panels.logging.LoggingPanel",
    # "debug_toolbar.panels.redirects.RedirectsPanel",
    # "debug_toolbar.panels.profiling.ProfilingPanel",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
] + MIDDLEWARE  # noqa: W0401

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}