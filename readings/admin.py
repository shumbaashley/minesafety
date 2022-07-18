from django.contrib import admin

from .models import Notepad, ReadingData

@admin.register(ReadingData)
class ReadingDataAdmin(admin.ModelAdmin):
    list_display = ("temperature", "humidity", "gas", "created")


@admin.register(Notepad)
class NotepadAdmin(admin.ModelAdmin):
    list_display = ("title", "note", "created")