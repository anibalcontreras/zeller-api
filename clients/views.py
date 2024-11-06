from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientListSerializer


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
