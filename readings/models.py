from django.db import models

from utils.models import TimeStampedUUIDModel


class ReadingData(TimeStampedUUIDModel):
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    gas = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        ordering = ['-created']
        verbose_name = "Data Reading"
        verbose_name_plural = "Data Readings"

    def __str__(self):
        return f'Reading - {self.id}'


class Notepad(TimeStampedUUIDModel):
    title = models.CharField(max_length=200)
    note = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-created']
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f'Note - {self.id}'

