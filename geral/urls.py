from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name ='home'),
    path("login", views.loginPage, name="login"),
    path("createuser", views.createUser, name='createuser'),
    path("buyingpage", views.buyingPage, name='buyingpage'),
    path("createproduct", views.newProduct, name='createproduct'),
    path('logout', views.sair, name='logout')
]