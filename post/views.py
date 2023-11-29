from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from comment.models import Comentario
from profiles.models import Profile


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


#def search_recipes(request):
 #   receta = Receta.objects.all()
  #  context = {'receta': receta}
   # return render(request,'search_recipes.html',context)

def search_recipes(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda de la URL

    # Buscar perfiles si la consulta comienza con "@"
    user_recipes = []
    profiles = []
    if query.startswith('@'):
        username_query = query[1:]
        profiles = User.objects.filter(username__icontains=username_query)
    else:
        user_recipes = Receta.objects.filter(name__icontains=query)

    context = {
        'user_recipes': user_recipes,
        'profiles': profiles,
    }

    return render(request, 'search_recipes.html', context)


def select_recipe(request, recipe_id):
    # Obtener la receta específica por su ID
    recipe = Receta.objects.get(pk=recipe_id)

    # Pasar la receta al contexto
    ingredients_list = recipe.ingredients.split('\n')
    
    context =  {'recipe': recipe, 'ingredients_list': ingredients_list}

    # Renderizar la plantilla con el contexto
    return render(request, 'select_recipe.html', context)


def view_comments(request,recipe_id):
    recipe = Receta.objects.get(pk=recipe_id)

    perfil_usuario = Profile.objects.get(user=request.user)


    comentarios = Comentario.objects.filter(receta=recipe)

    context = {'comentarios':comentarios,'perfil_usuario':perfil_usuario}

    return render(request,'comments.html',context)