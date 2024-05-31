from django.shortcuts import render,redirect
from .models import *
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login


# Create your views here.


#def register(request):
#    if request.method == 'POST':
#        form = UserRegistrationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            username=form.cleaned_data['username']
#            messages.success(request,f'Usuario {username} creado')
#            return redirect('login')
#    else:
#        form = UserRegistrationForm()
#    context= {'form':form}
#    return render(request,'login/register.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        agree_terms = request.POST.get('agree_terms', False)
        captcha = request.POST.get('captcha')

        print('Captcha:', captcha)
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Las contrasenas no coinciden')
            return redirect('register')  # Redirect to the registration page

        # Check if the terms and conditions are agreed
        if not agree_terms:
            messages.error(request, 'Please agree to the terms and conditions.')
            return redirect('register')  # Redirect to the registration page

        # Check if the reCAPTCHA is valid
        if not captcha:
            messages.error(request, 'Please complete the reCAPTCHA.')
            return redirect('register')  # Redirect to the registration page

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully. You can now log in.')

            login(request,user)
            return redirect('create_profile')  # Redirect to the login page
        except Exception as e:
            messages.error(request, f'Error creating account: {e}')
    else:
        form = UserRegistrationForm()

    return render(request, 'login/register.html', {'form': form})  # Adjust the template path accordingly

@login_required
def feed(request):
    return render(request,'login/feed.html')

