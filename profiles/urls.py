from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('edit_profile', views.edit_profile, name='edit_profile' ),
    path('view_profile', views.profile, name='view_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)