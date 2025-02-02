# filepath: /Users/obiajulu/moms_cake/cake_blog/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('', views.cake_blog, name='cake_blog'),
]