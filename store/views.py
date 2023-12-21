from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .forms import SignUpForm
from .models import Category, Product


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()[:5]
    return render(
        request, 'store/home.html',
        {'products': products, 'categories': categories,}
    )

def login_user(request):
    if request.user.is_authenticated:
        return redirect('store:home')

    categories = Category.objects.all()[:5]
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message='Welcome!')
            return redirect('store:home')
        else:
            messages.error(request, message='Wrong username or password. Try again.')
            return render(request, 'store/login.html', {'categories':categories,})
    else:
        return render(request, 'store/login.html', {'categories':categories,})

def logout_user(request):
    logout(request)
    return redirect('store:home')

def register_user(request):
    form = SignUpForm()
    categories = Category.objects.all()[:5]
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered! Welcome!')
            return redirect('store:home')
        else:
            messages.error(request, 'There was an error registering you. Please try again.')
            return redirect('store:register')
    return render(request, 'store/register.html', {'form': form, 'categories':categories,})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()[:5]
    return render(request, 'store/product.html', {'product': product, 'categories':categories,})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = get_list_or_404(Product, category=category)
    categories = Category.objects.all()[:5]
    return render(
        request, 'store/home.html',
        {'products': products, 'categories': categories,}
    )
