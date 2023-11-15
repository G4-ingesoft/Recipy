from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('feed', views.feed, name='feed'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)