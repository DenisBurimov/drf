from django.db import models
from users.models import BaseModel, Profile
from uuid import uuid4


class Article(BaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    users_liked = models.ManyToManyField(Profile, related_name="articles_liked")

    def __str__(self):
        return f"{self.title} by {self.author.first_name} {self.author.last_name}"
