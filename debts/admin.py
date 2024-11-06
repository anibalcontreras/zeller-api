from django.contrib import admin
from .models import Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'institution', 'amount', 'due_date')  # Campos visibles
    search_fields = ('client__name', 'institution')                       # Campos de búsqueda
    list_filter = ('institution', 'due_date')                             # Filtros por institución y fecha
