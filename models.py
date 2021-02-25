from django.db import models

# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)

class player(models.Model):
    playerid = models.ForeignKey(team, on_delete=models.CASCADE)
    playername = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
