from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Receta



# Create your views here.
@login_required
def feed(request):
    receta = Receta.objects.all()
    context = {'receta': receta}
    return render(request,'feed.html',context)

#def search_recipes(request):
 #   receta = Receta.objects.all()
  #  context = {'receta': receta}
   # return render(request,'search_recipes.html',context)

def search_recipes(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda de la URL
    user_recipes = Receta.objects.filter(name__icontains=query)
    
    context = {
        'user_recipes': user_recipes,
    }

    return render(request, 'search_recipes.html', context)