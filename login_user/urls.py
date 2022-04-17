from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
]