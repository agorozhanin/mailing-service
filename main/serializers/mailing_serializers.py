from rest_framework import serializers

from main.models import Mailing


class ModelMailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'
