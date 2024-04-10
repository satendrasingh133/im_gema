# Generated by Django 5.0.3 on 2024-04-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_remove_macbookinventry_usb_idf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='macbookinventry',
            name='datetime',
        ),
        migrations.AddField(
            model_name='macbookinventry',
            name='delivery_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='macbookinventry',
            name='shipment_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]