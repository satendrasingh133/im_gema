# Generated by Django 5.0.3 on 2024-04-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('serial_no', models.CharField(max_length=122)),
                ('status', models.CharField(max_length=122)),
                ('device_status', models.CharField(max_length=122)),
                ('created_at', models.DateField()),
                ('created_by', models.CharField(max_length=122)),
                ('updated_at', models.DateField()),
                ('updated_by', models.CharField(max_length=122)),
            ],
        ),
    ]
