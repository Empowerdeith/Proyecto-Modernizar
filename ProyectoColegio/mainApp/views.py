from django.shortcuts import render, HttpResponse
from .models import NivTransicion,EdBasica, Reglamento
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.


def home(request):
    return render(request, 'portada/portada.html')


def utiles(request):
    nivTransicion = NivTransicion.objects.all()
    edBasica = EdBasica.objects.all()
    return render(request, 'utiles/utiles.html', {'nivTransicion': nivTransicion, 'edBasica': edBasica})
    #block1=["Kínder","Pre Kínder","Colación"]
    
    #cursos = Cursos.objects.all()
    #return render(request, 'utiles/utiles.html', {'cursos': cursos, 'block1': block1})

@xframe_options_sameorigin
def reglamento(request):
    reglamento1= Reglamento.objects.all()
    return render(request, 'reglamento/reglamento.html', {'reglamento1': reglamento1})
