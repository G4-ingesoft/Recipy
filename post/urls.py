from django.urls import path
from . import views
from .views import RecetaListView, RecetaDetailView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('feed', views.feed, name='feed'),
    path('feed/', RecetaListView.as_view(), name='feed'),
    path('receta/<int:pk>/', RecetaDetailView.as_view(), name='receta-detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)