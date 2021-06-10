from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name='home')
    url(r'^/$', views.index, name='home'),
    path('/form/', views.form, name='form'),
    path('/transfers/', views.transfers, name="transfers"),
    path('', views.form_to_model, name="form_to_model"),
    path('/queries/', views.queries, name='queries'),
    path('/signup/', views.signup, name='signup')
]