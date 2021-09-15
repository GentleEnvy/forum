from django.db import models
from django.contrib.auth.models import User

__all__ = ['User', 'Tag', 'Discussion', 'Comment']


class Tag(models.Model):
    title = models.TextField()


class Discussion(models.Model):
    title = models.TextField()
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
