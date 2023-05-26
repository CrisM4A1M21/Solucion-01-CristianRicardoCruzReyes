from django.urls import path
from pokemon import views

urlpatterns = [
    path('pokemons_list/', views.pokemons_list, name='pokemons_list')
]