# Generated by Django 5.0.3 on 2024-04-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_macbookinventry_alter_deviceuser_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='macbookinventry',
            name='usb_idd',
            field=models.IntegerField(null=True),
        ),
    ]
