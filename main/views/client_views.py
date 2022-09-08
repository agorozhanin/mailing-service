from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from main.serializers.client_serializers import ModelClientSerializer
from main.services.client.selectors import get_all_clients


class ClientCreateAPIView(CreateAPIView):
    """
    Представление для создания клиента
    """
    serializer_class = ModelClientSerializer


class ClientUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    """
    Представление для обновления или удаления данных клиента
    происходит по его идентификатору
    """
    serializer_class = ModelClientSerializer
    queryset = get_all_clients()
