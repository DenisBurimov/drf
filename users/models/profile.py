from django.db import models
from .user import D3User


class Profile(models.Model):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    user = models.OneToOneField(D3User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
