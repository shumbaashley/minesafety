from rest_framework import status, viewsets
from readings.models import GasReading, HumidityReading, ReadingData, TemperatureReading
from readings.serializers import ReadingDataSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django_tables2 import SingleTableView
from .tables import ReadingDataTable
from django.views.generic import ListView
from .models import ReadingData


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        return [obj.created for obj in ReadingData.objects.all()][:10] 

    def get_providers(self):
        """Return names of datasets."""
        return ["Temperature", "Humidity", "Gas"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[obj.temperature for obj in ReadingData.objects.all()][:10] ,[obj.humidity for obj in ReadingData.objects.all()][:10] , [obj.gas for obj in ReadingData.objects.all()][:10] ]


dashboard_page =TemplateView.as_view(template_name="readings/dashboard.html")
line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

class PostDataReadings(APIView):
    queryset = ReadingData.objects.all().order_by('-created')
    serializer_class = ReadingDataSerializer
    permission_classes = []


    def post(self, request, format=None):
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


class GetCurrentReadings(APIView):
    def get(self, request, format=None):
        data = ReadingData.objects.first()
        serializer = ReadingDataSerializer(data)
        return Response(data=serializer.data)

    

# class ReadingDataListView(ListView):
#     model = ReadingData
#     template_name = 'readings/table.html'



class ReadingDataListView(SingleTableView):
    model = ReadingData
    table_class = ReadingDataTable
    template_name = 'readings/tables-data.html'
