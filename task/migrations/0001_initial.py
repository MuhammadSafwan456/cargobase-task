# Generated by Django 3.2.12 on 2022-08-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=10)),
                ('flight_number', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('info', models.JSONField()),
            ],
        ),
    ]
