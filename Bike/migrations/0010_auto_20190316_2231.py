# Generated by Django 2.1.5 on 2019-03-16 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bike', '0009_auto_20190316_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='cm_last_insert_dttm',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]