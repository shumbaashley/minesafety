import django_tables2 as tables

from users.models import User
from .models import ReadingData

class ReadingDataTable(tables.Table):
    class Meta:
        model = ReadingData
        template_name = "django_tables2/bootstrap4.html"
        fields = ("temperature", "humidity", "gas", "created")


class UsersTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap4.html"
        fields = ("first_name", "last_name", "username", "date_joined")
