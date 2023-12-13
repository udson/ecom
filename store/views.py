from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Product


def home(request):
  products = Product.objects.all()
  return render(request, 'store/mdb/home.html', {'products': products})

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
