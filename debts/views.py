from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DebtSerializer
from clients.models import Client

class DebtViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path=r'(?P<client_pk>[^/.]+)/debts')
    def create_debt(self, request, client_pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
        except Client.DoesNotExist:
            return Response({"detail": "Cliente no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DebtSerializer(data=request.data)
        if serializer.is_valid():
            # Asocia la deuda con el cliente y guarda
            serializer.save(client=client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
