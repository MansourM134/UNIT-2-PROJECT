from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def goals(request):
    return render(request, 'main/goals.html')


def focus(request):
    return render(request, 'main/focus.html')


def targets(request):
    return render(request, 'main/targets.html')


def baseline(request):
    return render(request, 'main/baseline.html')


def strategy(request):
    return render(request, 'main/strategy.html')


def initiatives(request):
    return render(request, 'main/initiatives.html')
