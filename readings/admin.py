from django.contrib import admin

from .models import Notepad, ReadingData
from .models import ThresholdSettings

admin.site.register(ThresholdSettings)
@admin.register(ReadingData)
class ReadingDataAdmin(admin.ModelAdmin):
    list_display = ("temperature", "humidity", "gas", "created")


@admin.register(Notepad)
class NotepadAdmin(admin.ModelAdmin):
    list_display = ("title", "note", "created")