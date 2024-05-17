import os
from datetime import timedelta
from celery import Celery
from main.logger import log
from main.apps.articles.models import Article

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks()


@app.task(bind=True)
def debug_task():
    articles = Article.objects.all()
    log(log.INFO, "Testing celery task")
    log(log.INFO, f"Total articles: {len(articles)}")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        timedelta(minutes=1),
        debug_task.s(),
        name="debug task"
    )
