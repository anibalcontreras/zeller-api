from rest_framework import serializers
from .models import Conversation
from datetime import datetime


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "text", "role", "sent_at"]
        read_only_fields = ["role", "sent_at"]

    def create(self, validated_data):
        # Establecer la fecha y hora actual para 'sent_at'
        validated_data['sent_at'] = datetime.now()
        # Establecer 'client' para el campo 'role'
        validated_data['role'] = 'client'
        return super().create(validated_data)
