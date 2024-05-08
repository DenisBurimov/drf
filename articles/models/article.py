from django.db import models
from users.models.profile import Profile
from uuid import uuid4


class Article(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid4)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    users_liked = models.ManyToManyField(Profile, related_name="articles_liked")

    def __str__(self):
        return f"{self.title} by {self.author.first_name} {self.author.last_name}"
