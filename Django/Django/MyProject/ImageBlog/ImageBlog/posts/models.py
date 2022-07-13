from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.jpg')
    likes = models.ManyToManyField(User,related_name='post_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Hardware(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField(blank=False)

