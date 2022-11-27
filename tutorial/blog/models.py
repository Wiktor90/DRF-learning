from datetime import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, blank=True),
    last_name = models.CharField(max_length=128, blank=True),
    email = models.EmailField(max_length=256)
    nick = models.CharField(max_length=64, blank=True),


class Post(models.Model):
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=256),
    text = models.TextField(blank=True),
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE),
    author = models.ForeignKey(Author, related_name="c_author", on_delete=models.CASCADE)
    text = models.TextField(blank=True),
    created_at = models.DateTimeField(default=datetime.now, blank=True)
