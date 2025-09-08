"""
URL configuration for backend_task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
    title="Swagger Doc for Technical Task",
    default_version='v1',
    description="This is Technical Task",
    terms_of_service="example.uz",
    contact=openapi.Contact(email="example@gmail.com"),
    ),
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui-v1"),
    path("api/v1/", include("main.apps.v1"), name="main"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)