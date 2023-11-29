from django.urls import path
from . import views

urlpatterns = [
    path('edit_profile', views.edit_profile, name='edit_profile' ),
    path('view_profile', views.profile, name='view_profile'),
    path('view_profile/<str:username>', views.view_profile, name='view_profile'),
] 