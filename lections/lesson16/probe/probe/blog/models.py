from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    likes = models.IntegerField(default=0)
