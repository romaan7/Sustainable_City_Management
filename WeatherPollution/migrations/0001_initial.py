# Generated by Django 2.1.7 on 2019-02-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station', models.CharField(max_length=50)),
                ('Temperature', models.IntegerField()),
                ('Weathercol', models.CharField(max_length=25)),
                ('windspeed', models.IntegerField()),
                ('windgust', models.IntegerField()),
                ('winddirection', models.CharField(max_length=10)),
                ('humidity', models.IntegerField()),
                ('rainfall', models.DecimalField(decimal_places=3, max_digits=9)),
                ('pressure', models.IntegerField()),
            ],
        ),
    ]