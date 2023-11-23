from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

from profiles.views import create_profile


urlpatterns = [
    path('', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('register', views.register,name='register'),
    path('create_profile',create_profile, name='create_profile'),
]