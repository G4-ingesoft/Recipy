from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import ProfileUpdateForm,ProfileCreateForm

from post.models import Receta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Si la solicitud es un POST, procesa el formulario de actualización del perfil
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('view_profile')  # Reemplaza 'view_profile' con la URL a la que deseas redirigir después de editar el perfil

    else:
        # Si la solicitud no es un POST, crea una instancia del formulario con la información actual del perfil
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Renderiza la plantilla con el formulario como parte del contexto
    return render(request, 'profile/edit_profile.html', {'p_form': p_form})

@login_required
def create_profile(request):
    if request.method == 'POST':
        # Si la solicitud es un POST, procesa el formulario de actualización del perfil
        p_form = ProfileCreateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('view_profile')  # Reemplaza 'view_profile' con la URL a la que deseas redirigir después de editar el perfil

    else:
        # Si la solicitud no es un POST, crea una instancia del formulario con la información actual del perfil
        p_form = ProfileCreateForm(instance=request.user.profile)

    # Renderiza la plantilla con el formulario como parte del contexto
    return render(request, 'profile/create_profile.html', {'p_form': p_form})

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

def view_profile(request, username):
    # Get the user object based on the provided username
    user = User.objects.get(username=username)

    # Obtain the profile associated with the user
    user_profile = user.profile

    # Get the recipes associated with the user profile
    user_recipes = Receta.objects.filter(user=user_profile)

    context = {
        'user_profile': user_profile,
        'user_recipes': user_recipes,
    }

    return render(request, 'profile/view_profile.html', context)