# Generated by Django 4.2.2 on 2023-07-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_rentalhistory_rental_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalhistory',
            name='rental_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
