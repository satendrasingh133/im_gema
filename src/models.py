from django.db import models

# Create your models here.
class Inventry(models.Model):
    type = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    serial_no = models.CharField(max_length=122)
    status = models.CharField(max_length=122)
    device_status = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=122)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=122)

class DeviceUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)