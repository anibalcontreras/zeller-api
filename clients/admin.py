from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rut')  # Campos que se mostrarán en la lista
    search_fields = ('name', 'rut')       # Campos por los cuales se puede buscar
