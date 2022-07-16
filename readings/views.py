from rest_framework import viewsets
from readings.models import ReadingData
from readings.serializers import ReadingDataSerializer


class ReadingDataViewSet(viewsets.ModelViewSet):
    queryset = ReadingData.objects.all().order_by('-created')
    serializer_class = ReadingDataSerializer
    permission_classes = []
