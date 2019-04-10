from django.urls import path
from . import views


urlpatterns = [
    path('', views.invioMail, name='mail_form'),
    path('mail_inviata/', views.mailInviata, name='mail_done'),
]