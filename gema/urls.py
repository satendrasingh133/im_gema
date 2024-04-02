from django.contrib import admin
from django.urls import path
from .views import create_deviceuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deviceuser/form/', create_deviceuser, name='deviceuser_form'),
]
