from django import template
from ..models import DeviceUser, Inventry, MacbookInventry, InventryType  # Import your model

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
def get_inventry_type_by_id(type):
    inventryType = InventryType.objects.get(pk=type)
    return inventryType.name

@register.filter
def get_breakfixMacbook(deviceuser_id):
    macbookData = MacbookInventry.objects.filter(deviceuser_id=deviceuser_id)
    if macbookData:
        for macbook in macbookData:
            macFilter = Inventry.objects.get(pk=macbook.macbook_id, status=3)
            if macFilter.name:
                return macFilter.name + " (" + macFilter.serial_no +")"
    else:
        return "na"

@register.filter
def get_breakfixMacbookId(deviceuser_id):
    macbookData = MacbookInventry.objects.filter(deviceuser_id=deviceuser_id)
    if macbookData:
        for macbook in macbookData:
            macFilter = Inventry.objects.get(pk=macbook.macbook_id, status=3)
            if macFilter.name:
                return macFilter.id
    else:
        return 0
