from django.db import models

from utils.models import TimeStampedUUIDModel

class Temperature(models.Model):
    actual = models.DecimalField(decimal_places=2, max_digits=10)
    reference = models.DecimalField(decimal_places=2, max_digits=10)
    recorded = models.DateTimeField()

    class Meta:
        verbose_name = "Temperature reading"
        verbose_name_plural = "Temperature readings"


    def __str__(self):
        return f'temp-{self.actual}'

    @property
    def deviation(self):
        return self.actual - self.reference

    @property
    def alarm(self):
        return self.actual > self.reference



class Methane(models.Model):
    actual = models.DecimalField(decimal_places=2, max_digits=10)
    reference = models.DecimalField(decimal_places=2, max_digits=10)
    recorded = models.DateTimeField()

    class Meta:
        verbose_name = "Methane gas reading"
        verbose_name_plural = "Methane gas readings"


    def __str__(self):
        return f'gas-{self.actual}'


    @property
    def deviation(self):
        return self.actual - self.reference

    @property
    def alarm(self):
        return self.actual > self.reference


class ReadingData(TimeStampedUUIDModel):
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    gas = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'Reading - {self.id}'

class TemperatureReading(TimeStampedUUIDModel):
    temperature = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Temperature Reading - {self.id}'

class HumidityReading(TimeStampedUUIDModel):
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Humidity Reading - {self.id}'

class GasReadingData(TimeStampedUUIDModel):
    gas = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'Gas Reading - {self.id}'

