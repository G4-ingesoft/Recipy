from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import ProfileUpdateForm

from post.models import Receta

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def edit_profile(request):
    p_form = ProfileUpdateForm()
    return render(request, 'profile/edit_profile.html')

@login_required
def profile(request):
    # Obtener el perfil del usuario actual
    user_profile = get_object_or_404(Profile, user=request.user)

    # Obtener las recetas asociadas al perfil del usuario actual
    user_recipes = Receta.objects.filter(user=user_profile)

    context = {
        'user_profile': user_profile,
        'user_recipes': user_recipes,
    }

    return render(request, 'profile/view_profile.html', context)

@login_required
def delete_profile(request):
    if request.user.is_authenticated and request.method == 'POST':
        request.user.delete()  
        return redirect('register')  # Reemplaza 'home' con la URL a la que deseas redirigir
    else:
        # Manejar el caso en el que el usuario no está autenticado o no está utilizando el método POST
        return redirect('login')  # Reemplaza 'login' con la URL de tu página de inicio de sesión