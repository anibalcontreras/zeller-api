from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientListSerializer
from rest_framework.decorators import action
from datetime import timedelta
from django.utils import timezone
from conversations.models import Conversation
from ai.prompts import system_prompt
from ai.utils import generate_ai_message


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "create":
            return ClientListSerializer
        return ClientSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(
            {"detail": "You are not allowed to delete clients."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    
    @action(detail=False, methods=['get'], url_path='to-do-follow-up')
    def clients_to_do_follow_up(self, request):
        seven_days_ago = timezone.now() - timedelta(days=7)
        clients = Client.objects.filter(conversations__sent_at__lt=seven_days_ago).distinct()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], url_path='generate-message')
    def generate_message(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"detail": "Cliente no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        # Verificar si el cliente tiene deudas
        client_has_debts = client.debts.exists()
        
        # Generar el mensaje usando OpenAI
        ai_message_content = generate_ai_message(client.name, client_has_debts)

        # Guardar el mensaje en el modelo Conversation o Message
        Conversation.objects.create(
            client=client,
            text=ai_message_content,
            role="assistant",
            sent_at=timezone.now()
        )

        # Devolver solo el texto del mensaje generado
        return Response({"text": ai_message_content}, status=status.HTTP_200_OK)
