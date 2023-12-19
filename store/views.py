from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message='Welcome!')
            return redirect('home')
        else:
            messages.error(request, message='Wrong username or password. Try again.')
            return render(request, 'store/login.html', {})
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request, ):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered! Welcome!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error registering you. Please try again.')
            return redirect('register')
    return render(request, 'store/register.html', {'form': form,})
