from django.db import models
from django import forms
# Create your models here.
# If we add any new class , attribute or function within this page ,we need to go to the cmd and write python manage.py makemigrations and python manage.py migrate

class team(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)

class player(models.Model):
    playerid = models.ForeignKey(team, on_delete=models.CASCADE)
    playername = models.CharField(max_length=500)
    position = models.CharField(max_length=500)

class grounds(models.Model):
    groundname = models.CharField(max_length=500)
    groundimage = models.TextField()

    def __str__(self):
        return self.groundname






