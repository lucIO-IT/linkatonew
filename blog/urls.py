from django.urls import path
from . import views

urlpatterns = [
    path('chi_siamo/', views.visualizzaChiSiamo, name='chi_siamo'),
    path('aziende/', views.visualizzaPerAziende, name='aziende'),
    path('elenco_corsi/', views.visualizzaTopNew, name='top_new'),
    path('articolo/2/', views.visualizzaCardSx, name='sx_new'),
    path('articolo/3/', views.visualizzaCardCc, name='cc_new'),
    path('articolo/4/', views.visualizzaCardDx, name='dx_new'),
    path('articoli/', views.ArticoloList.as_view(), name='articolo_list'),
    path('articoli/<title>', views.articoloView, name='articolo_view'),
]