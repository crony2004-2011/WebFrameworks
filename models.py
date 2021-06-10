from django.db import models

# Create your models here.
class formquery(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    Query = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class transfers(models.Model):
    team = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.player

