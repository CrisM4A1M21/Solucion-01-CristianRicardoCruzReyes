from django.contrib import admin
from .models import Owner
# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    fields = ("nombre", "pais", "descripcion", "edad", "vigente")
    list_display = ("nombre", "pais", "descripcion",)