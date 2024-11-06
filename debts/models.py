from django.db import models
from clients.models import Client


class Debt(models.Model):
    client = models.ForeignKey(Client, related_name="debts", on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    amount = models.IntegerField()
    due_date = models.DateField()
