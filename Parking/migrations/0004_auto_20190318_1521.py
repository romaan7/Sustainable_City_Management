# Generated by Django 2.1.5 on 2019-03-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0003_auto_20190317_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carparkdata',
            name='spaces',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
