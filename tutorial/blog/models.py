from uuid import uuid4
from datetime import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, blank=True, default="")
    last_name = models.CharField(max_length=128, blank=True, default="")
    email = models.EmailField(max_length=256)
    nick = models.CharField(max_length=64, blank=True, default="")

    def __str__(self, *args, **kwargs):
        full_name = self.name + self.last_name
        return full_name if full_name else self.nick

    def save(self, *args, **kwargs):
        if all([self.name == "", self.last_name == "", self.nick == ""]):
            self.nick = "RandomUser#" + str(uuid4())[:8]
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self, *args, **kwargs):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name="c_author", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
