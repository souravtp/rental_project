# Generated by Django 4.2.2 on 2023-07-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='location',
        ),
    ]