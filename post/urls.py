from django.urls import path
from . import views
from .views import RecetaListView, RecetaDetailView, RecetaCreateView, RecetaUpdateView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('feed', views.feed, name='feed'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('feed/', RecetaListView.as_view(), name='feed'),
    path('receta/<int:pk>/', RecetaDetailView.as_view(), name='receta_detail'),
    path('receta/new/', RecetaCreateView.as_view(), name='receta_create'),
    path('receta/<int:pk>/update/', RecetaUpdateView.as_view(), name='receta_update'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)