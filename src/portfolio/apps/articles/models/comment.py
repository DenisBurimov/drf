from django.db import models
from users.models import BaseModel, Profile
from uuid import uuid4


class Comment(BaseModel):
    text = models.TextField(max_length=1024)
    article = models.ForeignKey(
        "Article",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="answers",
        null=True,
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    users_liked = models.ManyToManyField(Profile, related_name="comments_liked")

    def __str__(self):
        return f"{self.uuid}: {self.article.title} by {self.author.first_name} {self.author.last_name}"