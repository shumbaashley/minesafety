from rest_framework import status, viewsets
from readings.models import GasReading, HumidityReading, ReadingData, TemperatureReading
from readings.serializers import ReadingDataSerializer
from rest_framework.response import Response


class ReadingDataViewSet(viewsets.ModelViewSet):
    queryset = ReadingData.objects.all().order_by('-created')
    serializer_class = ReadingDataSerializer
    permission_classes = []


    def create(self, request):
        temperature = request.data['temperature']
        humidity = request.data['humidity']
        gas = request.data['gas']



        serializer = ReadingDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            temperature_record = TemperatureReading(temperature=temperature)
            temperature_record.save()

            humidity_record = HumidityReading(humidity=humidity)
            humidity_record.save()

            gas_record = GasReading(gas=gas)
            gas_record.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)