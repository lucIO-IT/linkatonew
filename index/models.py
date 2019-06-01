from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from core.models import Corso, file_size

from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Il file è troppo grande: non può superare i 2 MiB.')


# Create your models here.

codice_meccanografico_validator = RegexValidator(
    regex=r'^[A-Z][0-9]*',
    message="Inserire il Codice Meccanografico della propria scuola, "
            "accertandosi che le prime due lettere inserite siano delle maiuscole"
)

def percorso_cartella_utenti(instance, filename):
    return 'Utenti/Avatar/{nome_utente}/{file}'.format(
        nome_utente=instance.user.first_name + instance.user.last_name,
        file=filename)

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
    scuola = models.CharField("Codice Meccanografico", max_length=16, blank=True, null=True,
                              validators=[codice_meccanografico_validator])

    def __str__(self):
        return self.user.first_name + self.user.last_name

    def school_name(self):
        scuola = Scuola.objects.filter(codice=self.scuola)
        return scuola

    def corsi(self):
        corsi = Corso.objects.filter(docente_corso=self.user)
        return corsi

    def corsi_progress(self, corso, progress):
        corso = Corso.objects.get(pk=corso)
        progress = progress
        if progress == 1:
            return corso

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=percorso_cartella_utenti, validators=[file_size])

    def __str__(self):
        return self.user.first_name + self.user.last_name