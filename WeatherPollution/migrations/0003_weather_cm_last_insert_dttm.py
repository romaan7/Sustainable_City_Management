# Generated by Django 2.1.5 on 2019-03-18 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherPollution', '0002_weather_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='cm_last_insert_dttm',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
