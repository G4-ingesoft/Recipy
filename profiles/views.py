from django.shortcuts import render,redirect
from .models import *
from .forms import ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def edit_profile(request):
    p_form = ProfileUpdateForm()
    return render(request, 'profile/edit_profile.html')

@login_required
def profile(request):
  #  p_form = ProfileUpdateForm()
    return render(request, 'profile/view_profile.html')