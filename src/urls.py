from django.contrib import admin
from django.urls import path
from src import views

urlpatterns = [
    path('addinventry/', views.add_inventry, name="add_inventry"),
    path('adddeviceuser/', views.create_deviceuser, name="add_deviceuser"),
    path('useroverview/', views.user_overview, name="user_overview"),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),    
    path('delete_user/<int:user_id>/', views.delete_deviceuser, name='delete_user')
]