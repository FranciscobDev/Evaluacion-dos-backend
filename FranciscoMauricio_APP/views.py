from django.shortcuts import render
from basse_datos_local import datos_generos

def Inicio(request):
    return render(request, "FranciscoMauricio_APP/home.html", {'generos': datos_generos})

def Accion(request):
    genero = next((g for g in datos_generos if g['id'] == 'accion'), None)
    return render(request, "FranciscoMauricio_APP/genero.html", {'genero': genero})

def CienciaFiccion(request):
    genero = next((g for g in datos_generos if g['id'] == 'ciencia-ficcion'), None)
    return render(request, "FranciscoMauricio_APP/genero.html", {'genero': genero})

def Comedia(request):
    genero = next((g for g in datos_generos if g['id'] == 'comedia'), None)
    return render(request, "FranciscoMauricio_APP/genero.html", {'genero': genero})

def Romance(request):
    genero = next((g for g in datos_generos if g['id'] == 'romance'), None)
    return render(request, "FranciscoMauricio_APP/genero.html", {'genero': genero})
