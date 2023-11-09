from django.shortcuts import render, HttpResponse
from .models import Reglamento, ToolsLeft, ToolsCenter, ToolsRight
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.


def home(request):
    return render(request, 'portada/portada.html')


def utiles(request):
    toolsLeft = ToolsLeft.objects.all
    toolsCenter = ToolsCenter.objects.all
    toolsRight = ToolsRight.objects.all
    return render(request, 'utiles/utiles.html', {'toolsLeft': toolsLeft, 'toolsCenter': toolsCenter, 'toolsRight':toolsRight})

@xframe_options_sameorigin
def reglamento(request):
    reglamento1= Reglamento.objects.all()
    return render(request, 'reglamento/reglamento.html', {'reglamento1': reglamento1})
