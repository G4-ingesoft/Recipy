from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .models import Receta

# Create your views here.
@login_required
def feed(request):
    receta = Receta.objects.all()
    context = {'receta': receta}
    return render(request,'feed.html',context)

class RecetaListView(ListView):
    model = Receta
    template_name = 'feed.html'
    context_object_name = 'receta'
    # ordering = ['-timestamp']

class RecetaDetailView(ListView):
    model = Receta
    template_name = 'receta_detail.html'
