from rest_framework import serializers
from .models import Conversation
from datetime import datetime


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "text", "role", "sent_at"]
        read_only_fields = ["role"]

    def create(self, validated_data):
        validated_data['role'] = 'client'
        return super().create(validated_data)
