from django.contrib import admin
from .models import Corso, Lezione, Risorsa

# Register your models here.


class CorsoModelAdmin(admin.ModelAdmin):
    model = Corso
    list_display = ["nome_corso", "img_corso", "descrizione_corso", "docente_corso", "data_corso"]
    search_fields = ["nome_corso", "docente_corso"]
    list_filter = ["data_corso"]

class LezioneModelAdmin(admin.ModelAdmin):
    model = Lezione
    list_display = ["nome_lezione", "link_lezione", "corso_lezione"]
    search_fields = ["nome_lezione", "corso_lezione"]
    list_filter = ["corso_lezione"]


admin.site.register(Corso, CorsoModelAdmin)
admin.site.register(Lezione, LezioneModelAdmin)
admin.site.register(Risorsa)
