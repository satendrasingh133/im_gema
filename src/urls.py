from django.contrib import admin
from django.urls import path
from src import views

urlpatterns = [
    path('addinventry/', views.add_inventry, name="add_inventry"),
    path('adddeviceuser/', views.create_deviceuser, name="add_deviceuser")
]