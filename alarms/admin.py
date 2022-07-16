from django.contrib import admin

from .models import Alarm

@admin.register(Alarm)
class Alarm(admin.ModelAdmin):
    list_display = ("metric", 'recorded')
