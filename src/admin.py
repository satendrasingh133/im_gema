from django.contrib import admin
from src.models import Inventry, DeviceUser, MacbookInventry

# Register your models here.
admin.site.register(Inventry)
admin.site.register(DeviceUser)
admin.site.register(MacbookInventry)