from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
