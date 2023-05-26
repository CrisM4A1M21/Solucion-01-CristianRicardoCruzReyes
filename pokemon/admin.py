from django.contrib import admin
from .models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    fields = ("nombre", "numero", "generacion","tipo",)
    list_display = ("nombre", "generacion", "tipo")
    search_fields = ("nombre",)
