from django.urls import path
from . import views


urlpatterns = [
    path('home/<token>/', views.listView, name='list_view'),
    path('profilo_utente/', views.accountProfileView, name='account_profile'),
    path('risultati_ricerca/', views.cerca, name='risultati_ricerca'),
    path('user/', views.docente_corsi, name='corsi_docente'),
    path('new_course/<int:token>', views.creaCorso, name='crea_corso'),
    path('new_course/preview/<int:pk>', views.previewCorso, name='preview_corso'),
    path('new_course/preview/<int:pk>/delete', views.eliminaLezione, name='elimina_lezione'),
    path('update_course/<int:pk>/modifica_corso/', views.FormModificaCorso.as_view(), name='modifica_corso'),
    path('ajax_copy_lesson/<int:lesson>/<int:course>', views.copyLesson, name='copia_lezione'),
    path('lista_corsi/miei_corsi/', views.visualizzaMieiMooc, name='miei_mooc'),
    path('lista_corsi/preferiti/', views.filtraCorsoPreferiti, name='corsi_preferiti'),
    path('course/<int:pk>', views.visualizzaCorso, name='finestra_corso'),
    path('course/<int:pk>/salva_preferiti/', views.salvaPreferiti, name='salva_preferiti'),
    path('lessons/<int:pk>', views.visualizzaLezione, name='finestra_lezione'),
    path('docenti/', views.lista_docenti, name='docenti'),
    path('ajax_request/<int:user>/<int:course>', views.ajax, name='ajax'),
    path('ajax_lezione/', views.ajax_lesson_form, name='ajax_lesson_form'),
]
