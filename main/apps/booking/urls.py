from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.booking_create_api_view, name='booking_create'),
    path('list/', views.booking_list_api_view, name='booking_list'),
    path('delete/<int:pk>/', views.booking_delete_api_view, name='booking_delete'),
]
