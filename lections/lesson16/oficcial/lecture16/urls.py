from django.urls import path
from lecture16 import views

urlpatterns = [
    path('', views.index, name='index'),
]
