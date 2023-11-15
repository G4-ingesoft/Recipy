from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('register', views.register,name='register'),
    path('feed', views.feed, name='feed'),
    path('edit_profile', views.profile, name='edit_profile' )
]