from rest_framework import serializers

from main.models import Message


class ModelMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
