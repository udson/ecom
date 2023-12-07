from django.shortcuts import redirect, render


def home(request):
    return render(request, 'store/home.html', {})
