# Generated by Django 5.0.3 on 2024-04-03 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_deviceuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceuser',
            name='contact_no',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', message='Phone number must be 10 digits.')]),
        ),
        migrations.AlterField(
            model_name='deviceuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]