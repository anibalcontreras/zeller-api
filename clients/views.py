from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientListSerializer
from rest_framework.decorators import action
from datetime import timedelta
from django.utils import timezone


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
