from django.utils import timezone
from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.jpg')

    def __str__(self):
        return self.title
