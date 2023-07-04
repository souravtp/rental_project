# Generated by Django 4.2.2 on 2023-07-02 10:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=150)),
                ('year', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('color', models.CharField(max_length=50)),
                ('fuel', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=20)),
                ('stars', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(5.0)])),
                ('availability', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
