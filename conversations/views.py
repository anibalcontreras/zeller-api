from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ConversationSerializer
from clients.models import Client

class ConversationViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path=r'(?P<client_pk>[^/.]+)/conversations')
    def create_conversation(self, request, client_pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
        except Client.DoesNotExist:
            return Response({"detail": "Cliente no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
