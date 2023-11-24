from django.contrib import admin
from django.urls import include, path
from geral import views;

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("geral.urls")),
]
