import django_tables2 as tables
from .models import ReadingData

class ReadingDataTable(tables.Table):
    class Meta:
        model = ReadingData
        template_name = "django_tables2/bootstrap.html"
        fields = ("temperature", "humidity", "gas", "created")