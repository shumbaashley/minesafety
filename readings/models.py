from django.db import models

from utils.models import TimeStampedUUIDModel

class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
class ThresholdSettings(SingletonBaseModel):
    minimum_temperature = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_temperature = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_humidity = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_humidity = models.DecimalField(max_digits=10, decimal_places=2)
    minimum_gas_level = models.DecimalField(max_digits=10, decimal_places=2)
    maximum_gas_level = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Base Settings"
        verbose_name_plural = "Base Settings"

    def __str__(self):
        return f'Base Settings'

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

