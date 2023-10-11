from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("utiles", views.utiles, name="utiles"),
    path("reglamento", views.reglamento, name="reglamento")
    
]
