from django.urls import path
from . import views

app_name = "FranciscoMauricio_APP"

urlpatterns = [
    path('', views.Inicio,name='Inicio'),

]