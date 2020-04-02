from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    context = {
            "post": posts,
            }
    return render(request, 'blog/blog.html', context)

#def blog(request):
#    return render(request, 'blog/blog.html')

def post(request, post_id):
    context={
            'post_id': post_id
            }
    return render(request, 'blog/post.html', context)

def new_post(request):
    return render(request, 'blog/new_post.html')
