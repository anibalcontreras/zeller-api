from rest_framework import serializers
from .models import Client
from conversations.serializers import ConversationSerializer
from debts.serializers import DebtSerializer
import re


class ClientSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True, read_only=True)
    debts = DebtSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ["id", "name", "rut", "conversations", "debts"]


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "rut"]

    def validate_rut(self, value):
        if not re.match(r"^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$", value):
            raise serializers.ValidationError("Invalid RUT")
        return value
