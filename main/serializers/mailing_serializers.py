from rest_framework import serializers

from main.models import Mailing
from main.services.message.selectors import get_all_messages_by_mailing


class ModelMailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class StatisticsMailingSerializer(serializers.ModelSerializer):
    count_messages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mailing
        fields = ("id",
                  "start_date",
                  "end_date",
                  "code_phone",
                  "tag",
                  "message_text",
                  "count_messages")

    def get_count_messages(self, instance):
        return get_all_messages_by_mailing(mailing=instance).count()
