from datetime import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, blank=True, default=""),
    last_name = models.CharField(max_length=128, blank=True, default=""),
    email = models.EmailField(max_length=256)
    nick = models.CharField(max_length=64, blank=True, default=""),

    def __str__(self, *args, **kwargs):
        return f"{self.name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.name and not self.last_name:
            self.nick = "RandomUser-" + str(self.pk)
        super().save(self, *args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=256),
    text = models.TextField(blank=True, default=""),
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE),
    author = models.ForeignKey(Author, related_name="c_author", on_delete=models.CASCADE)
    text = models.TextField(blank=True, default=""),
    created_at = models.DateTimeField(default=datetime.now, blank=True)
