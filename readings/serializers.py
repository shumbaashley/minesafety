from readings.models import ReadingData
from rest_framework import serializers


class ReadingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingData
        fields = '__all__'
