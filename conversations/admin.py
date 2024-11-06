from django.contrib import admin
from .models import Conversation

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'role', 'sent_at')  # Campos visibles en la lista
    search_fields = ('client__name', 'text')            # Campos de búsqueda
    list_filter = ('role', 'sent_at')                   # Filtros por rol y fecha
