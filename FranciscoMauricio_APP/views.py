from django.shortcuts import render

# Base de datos simulada
datos_generos = [
    {
        'id': 'accion',
        'nombre': 'Acción',
        'descripcion': 'Películas llenas de adrenalina, explosiones y persecuciones emocionantes.',
        'peliculas': [
            {'nombre': 'Mad Max: Fury Road', 'año': 2015, 'imagen': 'movie.jpg'},
            {'nombre': 'Die Hard', 'año': 1988, 'imagen': 'movie.jpg'},
            {'nombre': 'John Wick', 'año': 2014, 'imagen': 'movie.jpg'},
            {'nombre': 'Gladiator', 'año': 2000, 'imagen': 'movie.jpg'},
            {'nombre': 'The Dark Knight', 'año': 2008, 'imagen': 'movie.jpg'},
            {'nombre': 'Inception', 'año': 2010, 'imagen': 'movie.jpg'},
            {'nombre': 'Terminator 2: Judgment Day', 'año': 1991, 'imagen': 'movie.jpg'},
            {'nombre': 'The Matrix', 'año': 1999, 'imagen': 'movie.jpg'},
            {'nombre': 'Avengers: Endgame', 'año': 2019, 'imagen': 'movie.jpg'},
            {'nombre': 'Mission: Impossible - Fallout', 'año': 2018, 'imagen': 'movie.jpg'}
        ]
    },
    {
        'id': 'ciencia-ficcion',
        'nombre': 'Ciencia Ficción',
        'descripcion': 'Explora mundos futuros, tecnología avanzada y viajes espaciales.',
        'peliculas': [
            {'nombre': 'Interstellar', 'año': 2014, 'imagen': 'movie.jpg'},
            {'nombre': 'Blade Runner 2049', 'año': 2017, 'imagen': 'movie.jpg'},
            {'nombre': 'Dune', 'año': 2021, 'imagen': 'movie.jpg'},
            {'nombre': 'Star Wars: A New Hope', 'año': 1977, 'imagen': 'movie.jpg'},
            {'nombre': 'Alien', 'año': 1979, 'imagen': 'movie.jpg'},
            {'nombre': '2001: A Space Odyssey', 'año': 1968, 'imagen': 'movie.jpg'},
            {'nombre': 'Arrival', 'año': 2016, 'imagen': 'movie.jpg'},
            {'nombre': 'The Martian', 'año': 2015, 'imagen': 'movie.jpg'},
            {'nombre': 'Gravity', 'año': 2013, 'imagen': 'movie.jpg'},
            {'nombre': 'Avatar', 'año': 2009, 'imagen': 'movie.jpg'}
        ]
    },
    {
        'id': 'comedia',
        'nombre': 'Comedia',
        'descripcion': 'Historias divertidas diseñadas para hacerte reír a carcajadas.',
        'peliculas': [
            {'nombre': 'Superbad', 'año': 2007, 'imagen': 'movie.jpg'},
            {'nombre': 'Step Brothers', 'año': 2008, 'imagen': 'movie.jpg'},
            {'nombre': 'The Hangover', 'año': 2009, 'imagen': 'movie.jpg'},
            {'nombre': 'Anchorman', 'año': 2004, 'imagen': 'movie.jpg'},
            {'nombre': 'Tropic Thunder', 'año': 2008, 'imagen': 'movie.jpg'},
            {'nombre': 'Mean Girls', 'año': 2004, 'imagen': 'movie.jpg'},
            {'nombre': 'Dumb and Dumber', 'año': 1994, 'imagen': 'movie.jpg'},
            {'nombre': 'Ghostbusters', 'año': 1984, 'imagen': 'movie.jpg'},
            {'nombre': 'Shaun of the Dead', 'año': 2004, 'imagen': 'movie.jpg'},
            {'nombre': 'Hot Fuzz', 'año': 2007, 'imagen': 'movie.jpg'}
        ]
    },
    {
        'id': 'romance',
        'nombre': 'Romance',
        'descripcion': 'Historias de amor, pasión y relaciones conmovedoras.',
        'peliculas': [
            {'nombre': 'Titanic', 'año': 1997, 'imagen': 'movie.jpg'},
            {'nombre': 'The Notebook', 'año': 2004, 'imagen': 'movie.jpg'},
            {'nombre': 'Pride and Prejudice', 'año': 2005, 'imagen': 'movie.jpg'},
            {'nombre': 'La La Land', 'año': 2016, 'imagen': 'movie.jpg'},
            {'nombre': 'A Walk to Remember', 'año': 2002, 'imagen': 'movie.jpg'},
            {'nombre': 'Before Sunrise', 'año': 1995, 'imagen': 'movie.jpg'},
            {'nombre': 'Notting Hill', 'año': 1999, 'imagen': 'movie.jpg'},
            {'nombre': 'Crazy, Stupid, Love', 'año': 2011, 'imagen': 'movie.jpg'},
            {'nombre': '500 Days of Summer', 'año': 2009, 'imagen': 'movie.jpg'},
            {'nombre': 'The Fault in Our Stars', 'año': 2014, 'imagen': 'movie.jpg'}
        ]
    }
]

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