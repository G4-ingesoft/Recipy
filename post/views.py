from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Receta



# Create your views here.
@login_required
def feed(request):
    receta = Receta.objects.all()
    context = {'receta': receta}
    return render(request,'feed.html',context)