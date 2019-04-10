from django.contrib import admin
from .models import Scuola, Utente

# Register your models here.

class ScuolaModelAdmin(admin.ModelAdmin):

    model = Scuola
    list_display = ['regione', 'provincia', 'nome_scuola']
    list_display_links = ['nome_scuola']
    search_fields = ['nome_scuola', 'docenti_scuola']
    list_filter = ['nome_scuola', 'regione', 'provincia']


admin.site.register(Utente)
admin.site.register(Scuola, ScuolaModelAdmin)
