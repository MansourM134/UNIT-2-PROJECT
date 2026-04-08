from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request:HttpRequest):
    return render(request, 'main/home.html')

def preparations(request):
    return render(request, 'main/preparations.html')

def umrah_steps(request):
    return render(request, 'main/umrah_steps.html')

def general_info(request):
    return render(request, 'main/general_info.html')

def map_locations(request):
    return render(request, 'main/map_locations.html')

def how_to_use(request):
    return render(request, 'main/how_to_use.html')