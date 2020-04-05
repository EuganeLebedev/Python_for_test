from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    topic = models.ManyToManyField('Topic')
    title = models.CharField(max_length=150)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True) 
    update_date = models.DateTimeField(auto_now=True) 

class Author(models.Model):
    nickname = models.CharField(max_length=50, null=False, primary_key=True)
    user_name = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True) 
    update_date = models.DateTimeField(auto_now=True) 

class Topic(models.Model):
    topic = models.CharField(max_length=25)

