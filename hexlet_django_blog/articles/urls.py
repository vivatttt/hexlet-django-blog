from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.articles import views

urlpatterns = [

    path('', views.articles)

]
