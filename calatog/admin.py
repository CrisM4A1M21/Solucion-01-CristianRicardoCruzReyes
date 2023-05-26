from django.contrib import admin
from .models import Calatog
# Register your models here.

@admin.register(Calatog)
class CalatogAdmin(admin.ModelAdmin):
    fields = ("campo1",)
    list_display = ("campo1",)
