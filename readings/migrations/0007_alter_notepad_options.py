# Generated by Django 4.0.6 on 2022-07-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0006_notepad_delete_gasreading_delete_humidityreading_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notepad',
            options={'ordering': ['-created'], 'verbose_name': 'Note', 'verbose_name_plural': 'Notes'},
        ),
    ]