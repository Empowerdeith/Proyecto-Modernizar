from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'portada/portada.html')

def utiles(request):
    return render(request, 'utiles/utiles.html')

def reglamento(request):
    return render(request, 'reglamento/reglamento.html')