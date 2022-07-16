from django.contrib import admin

from .models import ReadingData, Temperature, Methane

@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ("actual", "reference", "deviation", 'recorded', "alarm")


@admin.register(Methane)
class MethaneAdmin(admin.ModelAdmin):
    list_display = ("actual", "reference", "deviation", 'recorded', "alarm")


@admin.register(ReadingData)
class ReadingDataAdmin(admin.ModelAdmin):
    list_display = ("temperature", "humidity", "gas", "created")