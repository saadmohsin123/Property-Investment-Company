from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User


def index(request):
    
    return render(request, 'propertyrader/index.html')

@login_required
def dashboard(request):
    
    ctx = {"username": request.user.user_name }
    
    return render(request, 'propertyrader/dashboard/dashboard.html', ctx)


def register(request):

    if request.method == 'POST':

        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        phone_number = request.POST["phone_number"]
        password = request.POST["password"]

         # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please choose a different email.')
            return HttpResponseRedirect(reverse('register'))


        User.objects.create_user(
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                user_name=username,
                                phone_number=phone_number,
                                password=password
                                        )
        messages.success(request, 'User registered successfully. Login to access your dashboard')
        return HttpResponseRedirect(reverse('login'))
            
    return render(request, 'propertyrader/register/register.html')


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user:
            # A backend authenticated the credentials
            auth_login(request, user)
            messages.success(request, 'Logged in successfully.')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.warning(request, 'Login Failed. Email and/or password is incorrect.')
            
    return render(request, 'propertyrader/login/login.html')


def logout(request):

    auth_logout(request)
    messages.success(request, 'Logged out successfully.')
    return HttpResponseRedirect(reverse('login'))
