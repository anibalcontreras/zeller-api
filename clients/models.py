from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
