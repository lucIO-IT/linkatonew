from django.urls import path
from .views import indexView, registrazioneUtente, cercaHome, datiScuola, avatar, UpdateAvatar #, prova_json_scuole

urlpatterns = [
    path('', indexView, name='homepage'),
    path('registrazione/', registrazioneUtente, name='registrazione'),
    path('registrazione/avatar/', avatar, name='avatar'),
    path('registrazione/dati_scuola/', datiScuola, name='registrazione_dati_utente'),
    path('risultati_ricerca/', cercaHome, name='risultati_ricerca_home'),
    path('modifica_foto/<int:pk>', UpdateAvatar.as_view(), name='update_avatar'),
    #path('prova_json/<code>', prova_json_scuole, name='prova_json'),
]