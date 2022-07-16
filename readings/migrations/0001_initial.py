# Generated by Django 3.2.3 on 2022-05-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Methane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reference', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recorded', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Methane gas reading',
                'verbose_name_plural': 'Methane gas readings',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reference', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recorded', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Temperature reading',
                'verbose_name_plural': 'Temperature readings',
            },
        ),
    ]
