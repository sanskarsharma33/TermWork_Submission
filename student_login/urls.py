from django.contrib import admin
from django.urls import path
from .models import UserDetails
from rest_framework.generics import ListCreateAPIView
from student_login.serializers import UserSerializer
from student_login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginpage/', views.Login, name='login'),
    path('auth/', views.auth_view, name='auth'),
    path('registeration/', views.registerpage, name='register'),
]
