from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path('', views.blog, name='blog'),
    path('post-<int:post_id>', views.post, name='post'),
    path('new_post', views.new_post, name='new_post'),
]
