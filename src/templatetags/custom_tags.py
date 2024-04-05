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
def get_totalLaptop(type):
    laptops = Inventry.objects.filter(type=type)
    return laptops.count()

