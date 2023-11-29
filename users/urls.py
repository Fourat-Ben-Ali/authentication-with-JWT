from django.contrib import admin
from django.urls import path
from .views import Register,login,user,logout
urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',login.as_view()),
    path('user/',user.as_view()),
    path('logout/',logout.as_view())
]