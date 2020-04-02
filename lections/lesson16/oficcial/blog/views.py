from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from blog.models import Post
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }

    return render(request, 'blog/blog.html', context)

def post(request, post_id):
    context = {
        'post_id': post_id,
    }

    return render(request, 'blog/post.html', context)

def new_post(request):
    if not request.method == 'POST':
        response = HttpResponse()
        response.status_code = 405
        return response

    title = request.POST['title']
    content = request.POST['content']

    post = Post(title=title, content=content)
    post.save()

    return HttpResponseRedirect(reverse('blog:blog'))
