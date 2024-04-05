# Generated by Django 5.0.3 on 2024-04-05 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', message='Phone number must be 10 digits.')])),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('serial_no', models.CharField(max_length=122)),
                ('status', models.IntegerField()),
                ('device_status', models.CharField(max_length=122)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=122)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='MacbookInventry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceuser_id', models.IntegerField()),
                ('macbook_id', models.IntegerField()),
                ('usb_id', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('photo', models.CharField(max_length=200)),
                ('tracking_no', models.CharField(max_length=20)),
                ('other_info', models.TextField()),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=122)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=122)),
            ],
        ),
    ]
