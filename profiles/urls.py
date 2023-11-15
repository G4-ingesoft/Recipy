from django.urls import path
from . import views

urlpatterns = [
    path('edit_profile', views.profile, name='edit_profile' ),
]