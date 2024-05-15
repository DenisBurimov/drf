from django.utils import timezone
from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid4)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
