from django.shortcuts import render

from blog.models import Post

# Create your views here.


from django.http import HttpResponse

def index(request):
    context = {
            'post_id': 'My post id'
            }
    return render(request, 'blog/index.html', context=context)

def post(request):
    return render(request, 'blog/post.html')
