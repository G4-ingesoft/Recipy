from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    
    # Buscar perfiles si la consulta comienza con "@"
    profiles = []
    if query.startswith('@'):
        username_query = query[1:]
        profiles = User.objects.filter(username__icontains=username_query)

    context = {
        'user_recipes': user_recipes,
        'profiles': profiles,
    }

    return render(request, 'search_recipes.html', context)