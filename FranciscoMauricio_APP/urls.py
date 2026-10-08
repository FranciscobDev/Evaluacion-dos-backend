from django.urls import path
from . import views

app_name = "FranciscoMauricio_APP"

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('accion/', views.Accion, name='Accion'),
    path('ciencia-ficcion/', views.CienciaFiccion, name='CienciaFiccion'),
    path('comedia/', views.Comedia, name='Comedia'),
    path('romance/', views.Romance, name='Romance'),
]