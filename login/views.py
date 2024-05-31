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

from django.utils.html import escape

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')  # Use the same name as in your form
            password2 = form.cleaned_data.get('password2')
            agree_terms = request.POST.get('agree_terms', False)

            # Sanitize user input and check if it was sanitized
            sanitized_username = escape(username)
            sanitized_email = escape(email)
            
            if sanitized_username != username:
                messages.error(request, 'Invalid characters in username. Please enter a different username.')
                return redirect('register')
            if sanitized_email != email:
                messages.error(request, 'Invalid characters in email. Please enter a different email.')
                return redirect('register')
            
            if password != password2:
                messages.error(request, 'Passwords do not match. Please try again.')
                return redirect('register')

            # Check if the terms and conditions are agreed
            if not agree_terms:
                messages.error(request, 'Please agree to the terms and conditions.')
                return redirect('register')  # Redirect to the registration page

            # Create a new user
            try:
                user = User.objects.create_user(username=sanitized_username, email=sanitized_email, password=password)
                user.save()
                messages.success(request, 'Account created successfully. You can now log in.')

                login(request,user)
                return redirect('create_profile')  # Redirect to the login page
            except Exception as e:
                messages.error(request, f'Error creating account: {e}')
        else:
            messages.error(request, 'Invalid form. Please try again.')
    else:
        form = UserRegistrationForm()

    return render(request, 'login/register.html', {'form': form})  # Adjust the template path accordingly


@login_required
def feed(request):
    return render(request,'login/feed.html')

