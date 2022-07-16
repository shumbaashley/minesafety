from django.db import models


class Alarm(models.Model):
    READINGS = (
        ('methane', 'Methane'),
        ('temperature', 'Temperature')
    )
    metric = models.CharField(choices=READINGS, max_length=12, default='methane')
    recorded = models.DateTimeField()

    def __str__(self):
        return f'{self.metric} alarm'

