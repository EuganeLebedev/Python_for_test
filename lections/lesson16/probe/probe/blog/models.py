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

    def __str__(self):
        return f'{self.id} {self.title}'

class Author(models.Model):
    nickname = models.CharField(max_length=50, null=False, primary_key=True)
    user_name = models.CharField(max_length=30)
    user_lastname = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)

    def __str__(self):
        return f'{self.nickname}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.TextField() 
    create_date = models.DateTimeField(auto_now_add=True) 
    update_date = models.DateTimeField(auto_now=True) 

    @property
    def short_comment(self):
        return self.comment[:25]


    def __str__(self):
        return f'{self.author} to post: {self.post} {self.short_comment}'

class Topic(models.Model):
    topic = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.topic}'

