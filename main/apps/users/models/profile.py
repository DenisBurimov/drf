from django.db import models
from .base_model import BaseModel
from .user import User


class Profile(BaseModel):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
