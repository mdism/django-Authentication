from django.urls import path
from . import views

APP_NAME= 'devices'

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('add/', views.add_device, name='add_device'),
    path('<int:pk>/edit/', views.edit_device, name='edit_device'),
    path('<int:pk>/delete/', views.delete_device, name='delete_device'),
    path('write_device_data/', views.write_device_data, name='write_device_data'),
    path('show_device_data/', views.show_device_data, name='show_device_data'),    
]
