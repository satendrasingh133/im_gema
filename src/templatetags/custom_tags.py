from django import template
from ..models import DeviceUser, Inventry  # Import your model

register = template.Library()

@register.filter
def get_username_from_id(user_id):
    user = DeviceUser.objects.get(pk=user_id)
    return user.name

@register.filter
def get_devicename_from_id(user_id):
    inventry = Inventry.objects.get(pk=user_id)
    return inventry.name

@register.filter
def get_deviceserial_no_from_id(user_id):
    inventry = Inventry.objects.get(pk=user_id)
    return inventry.serial_no

@register.filter
def get_total(type):
    laptops = Inventry.objects.filter(type=type)
    return laptops.count() if laptops.count() else 0

@register.filter
def get_available(type):
    data = Inventry.objects.filter(type=type, status__in=[1, 2])
    return data.count() if data.exists() else 0

@register.filter
def get_device_status(device_id): 
    inventry = Inventry.objects.get(pk=device_id)
    return inventry.status

@register.filter
def get_available_laptop_serial_numbers(type):   
    laptops = Inventry.objects.filter(type=type, status__in=[1, 2])
    return laptops
