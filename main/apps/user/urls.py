from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.user_create_api_view, name='user_create'),
    path('register/', views.user_registration_api_view, name='register'),
    path('login/', views.user_login_api_view, name='login'),
]
