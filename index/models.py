from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
#from core.models import Corso


# Create your models here.

codice_meccanografico_validator = RegexValidator(
    regex=r'^[A-Z][0-9]*',
    message="Inserire il Codice Meccanografico della propria scuola, "
            "accertandosi che le prime due lettere inserite siano delle maiuscole"
)


class Scuola(models.Model):
    nome_scuola = models.CharField(max_length=200, blank=True, null=True)
    regione = models.CharField(max_length=100, blank=True, null=True)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    docenti_scuola = models.ManyToManyField(User, related_name="Docenti")
    codice = models.CharField("Codice Meccanografico", max_length=8, blank=True, null=True,
                              validators=[codice_meccanografico_validator])

    def __str__(self):
        return self.codice

    class Meta:
        verbose_name = "Scuola"
        verbose_name_plural = "Scuole"


class Utente(models.Model):

    GENERE=(('f', 'femmina'), ('m', 'maschio'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genere = models.CharField(max_length=1, choices=GENERE, blank=True, null=True)
    data_nascita = models.DateField(blank=True, null=True)
    scuola = models.CharField("Codice Meccanografico", max_length=8, blank=True, null=True,
                              validators=[codice_meccanografico_validator])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"