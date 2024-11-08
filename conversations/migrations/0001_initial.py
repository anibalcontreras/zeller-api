# Generated by Django 5.1.3 on 2024-11-06 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conversation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                (
                    "role",
                    models.CharField(
                        choices=[("client", "client"), ("agent", "agent")],
                        max_length=10,
                    ),
                ),
                ("sent_at", models.DateTimeField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conversations",
                        to="clients.client",
                    ),
                ),
            ],
        ),
    ]
