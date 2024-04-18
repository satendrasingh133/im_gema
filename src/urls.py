from django.contrib import admin
from django.urls import path
from src import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('inventry/', views.list_inventry, name="list_inventry"),
    path('inventryType/', views.inventry_type, name="inventry_type"),
    path('addInventryType/', views.addinventry_type, name="addinventry_type"),
    path('getInventryTypeById/<int:inventryType_id>/', views.getInventryTypeById, name="getInventryTypeById"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addinventry/', views.add_inventry, name="add_inventry"),
    path('update_inventry/<int:inventry_id>/', views.get_inventry_by_id, name="update_inventry"),
    path('delete_inventry/<int:inventry_id>/', views.delete_inventry, name="delete_inventry"),
    path('update_inventry_data/', views.update_inventry_data, name="update_inventry_data"),
    path('adddeviceuser/', views.create_deviceuser, name="add_deviceuser"),
    path('useroverview/', views.user_overview, name="user_overview"),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_deviceuser, name='delete_user'),
    path('assign_macbook/', views.assign_macbook, name='assign_macbook'),
    path('logout/', views.logout_view, name='logout'),
    path('update_macbook/<int:id>/', views.update_macbook_by_id, name='update_macbook'),
    path('update_macbook_by_id/', views.update_assign_macbook, name='update_macbook_by_id'),
    path('render_modal_html/', views.render_modal_html, name='render_modal_html'),
    path('get_user_data/', views.get_user_data, name='get_user_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)