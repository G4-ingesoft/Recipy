from django.shortcuts import render,redirect
from .models import *
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,'login/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context= {'form':form}
    return render(request,'login/register.html',context)

def feed(request):
    return render(request,'login/feed.html')