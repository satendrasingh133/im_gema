from django.db import models
from django.core.validators import RegexValidator
 
# Create your models here.
# Status: 0 (not avaulable) , 1 (available), 2 (Returned) , 3 (Beakfix)
class Inventry(models.Model):
    type = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    serial_no = models.CharField(max_length=122)
    STATUS_CHOICES = (
        (0, 'Not Available'),
        (1, 'Available'),
        (2, 'Returned'),
        (3, 'Breakfix')
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    device_status = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=122)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=122)
 
# status: 0(assigned ), 1(fresh user), 2 (Resigined), 3 (Breakfix)
class DeviceUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be 10 digits.')], unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    STATUS_CHOICES = (
        (0, 'Assigned'),
        (1, 'Fresh User'),
        (2, 'Resigned'),
        (3, 'Breakfix')
    )
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)