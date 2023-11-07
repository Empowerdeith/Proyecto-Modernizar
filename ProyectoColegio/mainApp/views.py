from django.shortcuts import render, HttpResponse
from .models import Cursos, Reglamento
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.


def home(request):
    return render(request, 'portada/portada.html')


def utiles(request):
    cursos = Cursos.objects.all()
    return render(request, 'utiles/utiles.html', {'cursos': cursos})

@xframe_options_sameorigin
def reglamento(request):
    reglamento1= Reglamento.objects.all()
    return render(request, 'reglamento/reglamento.html', {'reglamento1': reglamento1})
