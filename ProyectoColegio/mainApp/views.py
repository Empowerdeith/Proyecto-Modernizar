from django.shortcuts import render, HttpResponse
from .models import Cursos

# Create your views here.


def home(request):
    return render(request, 'portada/portada.html')


def utiles(request):
    cursos = Cursos.objects.all()
    return render(request, 'utiles/utiles.html', {'cursos': cursos})


def reglamento(request):
    return render(request, 'reglamento/reglamento.html')
