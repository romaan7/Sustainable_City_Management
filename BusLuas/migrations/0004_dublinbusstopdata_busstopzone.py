# Generated by Django 2.2 on 2019-04-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusLuas', '0003_dublinbusrealtimestopdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='dublinbusstopdata',
            name='BusStopZone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
