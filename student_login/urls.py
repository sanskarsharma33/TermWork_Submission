from django.contrib import admin
from django.urls import path
from .models import UserDetails
from rest_framework.generics import ListCreateAPIView
from student_login.serializers import UserSerializer
from student_login import views
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginpage/', views.Login, name='login'),
    path('auth/', views.auth_view, name='auth'),
    path('change_profile/', views.change_profilepage, name='change_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('logout/',views.Logout,name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
]
