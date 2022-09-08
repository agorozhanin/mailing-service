from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from main.serializers.mailing_serializers import StatisticsMailingSerializer
from main.serializers.message_serializers import ModelMessageSerializer
from main.services.mailing.selectors import get_all_mailings, get_mailing_by_id
from main.services.message.selectors import get_all_messages, get_all_messages_by_mailing


class MailingStatisticsListAPIView(ListAPIView):
    """
    Представление для отображения общей
    статистики по рассылкам и количеству сообщений
    """
    serializer_class = StatisticsMailingSerializer
    queryset = get_all_mailings()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        output_data = serializer.data
        output_data.append({'general_messages_count': get_all_messages().count()})
        return Response(output_data)


class MailingStatisticsRetrieveAPIView(ListAPIView):
    """
    Представление для отображения всех сообщений
    конкретной рассылки
    """
    serializer_class = ModelMessageSerializer
    queryset = get_all_messages()

    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = get_all_messages_by_mailing(mailing=get_mailing_by_id(mailing_id=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
