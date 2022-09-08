from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from main.serializers.mailing_serializers import ModelMailingSerializer
from main.services.mailing.selectors import get_all_mailings


class MailingCreateAPIView(CreateAPIView):
    """
    Представление для создания рассылки
    """
    serializer_class = ModelMailingSerializer


class MailingUpdateDestroyAPIView(UpdateAPIView, DestroyAPIView):
    """
    Представление для обновления или удаления данных рассылки
    происходит по её идентификатору
    """
    serializer_class = ModelMailingSerializer
    queryset = get_all_mailings()
