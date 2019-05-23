from django.urls import path
from . import views


urlpatterns = [
    path('profilo_utente/', views.accountProfileView, name='account_profile'),
    path('risultati_ricerca/', views.cerca, name='risultati_ricerca'),
    path('docente/', views.docente_corsi, name='corsi_docente'),
    path('nuovo_corso/', views.creaCorso, name='crea_corso'),
    path('nuovo_corso/preview/<int:pk>', views.previewCorso, name='preview_corso'),
    path('nuovo_corso/preview/<int:pk>/elimina_lezione', views.eliminaLezione, name='elimina_lezione'),
    path('lista_corsi/miei_corsi/', views.visualizzaMieiMooc, name='miei_mooc'),
    path('lista_corsi/preferiti/', views.filtraCorsoPreferiti, name='corsi_preferiti'),
    path('corso/<int:pk>', views.visualizzaCorso, name='finestra_corso'),
    path('corso/<int:pk>/salva_preferiti/', views.salvaPreferiti, name='salva_preferiti'),
    path('user/corso/<int:pk>/modifca_corso/', views.FormModificaCorso.as_view(), name='modifica_corso'),
    path('lezioni/<int:pk>', views.visualizzaLezione, name='finestra_lezione'),
    path('docenti/', views.lista_docenti, name='docenti'),
    path('ajax_request/<int:user>/<int:course>', views.ajax, name='ajax'),
    path('ajax_lezione/', views.ajax_lesson_form, name='ajax_lesson_form'),
]
