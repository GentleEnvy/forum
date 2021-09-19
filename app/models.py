from django.contrib.auth.models import User
from django.db import models

__all__ = ['Forum', 'User', 'Tag', 'Discussion', 'Comment']


class Tag(models.Model):
    title = models.TextField(unique=True)


class Forum(models.Model):
    title = models.TextField(unique=True)


class Discussion(models.Model):
    title = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    text = models.TextField()
