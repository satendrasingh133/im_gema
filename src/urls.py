from django.contrib import admin
from django.urls import path
from src import views

urlpatterns = [
    path('inventry/', views.list_inventry, name="list_inventry"),
    path('addinventry/', views.add_inventry, name="add_inventry"),
    path('update_inventry/<int:inventry_id>/', views.get_inventry_by_id, name="update_inventry"),
    path('delete_inventry/<int:inventry_id>/', views.delete_inventry, name="delete_inventry"),
    path('update_inventry_data/', views.update_inventry_data, name="update_inventry_data"),
    path('adddeviceuser/', views.create_deviceuser, name="add_deviceuser")
]