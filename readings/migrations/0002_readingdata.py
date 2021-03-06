# Generated by Django 4.0.6 on 2022-07-16 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=10)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gas', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
