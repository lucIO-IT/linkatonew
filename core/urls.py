from django.urls import path
from . import views


urlpatterns = [
    path('profilo_utente/', views.accountProfileView, name='account_profile'),
    path('profilo_utente/elimina_profilo/<int:pk>', views.EliminaAccount.as_view(), name='elimina_account'),
    path('risultati_ricerca/', views.cerca, name='risultati_ricerca'),
    path('docente/', views.docente_corsi, name='corsi_docente'),
    path('nuovo_corso/', views.creaCorso, name='crea_corso'),
    path('nuovo_corso/preview/<int:pk>', views.previewCorso, name='preview_corso'),
    path('nuovo_corso/preview/<int:pk>/elimina_lezione', views.eliminaLezione, name='elimina_lezione'),
    #path('user/lista_corsi/', views.CorsiList.as_view(), name='corsi_list'),
    path('lista_corsi/', views.listaCorsi, name='corsi_list'),
    path('lista_corsi/miei_corsi/', views.visualizzaMieiMooc, name='miei_mooc'),
    path('lista_corsi/orientamento/', views.filtraCorsoOrientamento, name='corsi_orientamento'),
    path('lista_corsi/impresa/', views.filtraCorsoImpresa, name='corsi_impresa'),
    path('lista_corsi/digitale/', views.filtraCorsoDigitale, name='corsi_digitale'),
    path('lista_corsi/preferiti/', views.filtraCorsoPreferiti, name='corsi_preferiti'),
    path('corso/<int:pk>', views.visualizzaCorso, name='finestra_corso'),
    path('corso/<int:pk>/salva_preferiti/', views.salvaPreferiti, name='salva_preferiti'),
    path('corso/<int:pk>/cancella_preferiti/', views.cancellaPreferiti, name='cancella_preferiti'),
    path('user/corso/<int:pk>/modifca_corso/', views.FormModificaCorso.as_view(), name='modifica_corso'),
    path('corso/<int:pk>/cancella_corso/', views.eliminaCorso, name='cancella_corso'),
    path('lezioni/<int:pk>', views.visualizzaLezione, name='finestra_lezione'),
    path('docenti/', views.lista_docenti, name='docenti'),
    path('ajax_request/<int:user>/<int:course>', views.ajax, name='ajax'),
    path('ajax_lezione/', views.ajax_lesson_form, name='ajax_lesson_form'),
]
