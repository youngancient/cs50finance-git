from django import views
from django.urls import path
from .views import index, register,login, dashboard, logout
urlpatterns = [
    path('',index, name="home"),
    path('register',register, name="register"),
    path('login',login, name="login"),
    path('dashboard',dashboard, name="dashboard"),
    path('logout',logout, name="logout"),
]