from django.db import models
from clients.models import Client


class Conversation(models.Model):
    client = models.ForeignKey(
        Client, related_name="conversations", on_delete=models.CASCADE
    )
    text = models.TextField()
    role = models.CharField(
        max_length=10, choices=[("client", "client"), ("agent", "agent")]
    )
    sent_at = models.DateTimeField()
