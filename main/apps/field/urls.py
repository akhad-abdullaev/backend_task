from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.field_create_api_view, name='field_create'),
    path('list/', views.field_list_api_view, name='field_list'),
    path('update/<int:pk>/', views.field_update_api_view, name='field_update'),
    path('detail/<int:pk>/', views.field_detail_api_view, name='field_detail'),
]
