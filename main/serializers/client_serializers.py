from rest_framework import serializers

from main.models import Client


class ModelClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
