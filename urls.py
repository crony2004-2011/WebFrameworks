from django.contrib import admin
from django.conf.urls import include , url
from django.urls import path
from appdj import views
from . import views
urlpatterns = [
    url('^$', views.index),
]