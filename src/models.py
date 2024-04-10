from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
# Status: 0 (not avaulable) , 1 (available), 2 (Returned) , 3 (Beakfix)
class Inventry(models.Model):
    type = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    serial_no = models.CharField(max_length=122)
    status = models.IntegerField()
    device_status = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=122)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=122)

# status: 0(assigned ), 1(fresh user), 2 (Resigined), 3 (Breakfix)
class DeviceUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure email uniqueness
    contact_no = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be 10 digits.')], unique=True)  # Ensure phone number uniqueness
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

# macbook_id=inventry_id and usb_id is also inventry id
class MacbookInventry(models.Model):
    deviceuser_id = models.IntegerField()
    macbook_id = models.IntegerField()
    usb_id = models.IntegerField()
    shipment_datetime = models.DateTimeField(null=True)
    delivery_datetime = models.DateTimeField(null=True)
    photo = models.CharField(max_length=200)
    tracking_no = models.CharField(max_length=20)
    other_info = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=122)
    updated_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=122)
