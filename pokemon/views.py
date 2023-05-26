from django.shortcuts import render
from .models import Pokemon
# Create your views here.

def pokemons_list(request):
    pokemons = Pokemon.objects.all()
    fuegos = Pokemon.objects.filter(tipo='Fuego')
    return render(request, 'pokemon/archivo.html', context={
        "pokemons": pokemons,
        "fuegos": fuegos
    })
