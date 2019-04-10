from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import logging
logr = logging.getLogger(__name__)

# Create your models here.

#embed code validator
embed_validator = RegexValidator(
    regex=r'^<iframe src="https://player.vimeo.com.[a-zA-Z"./:+=0-9>< -?!\n]+$',
    message="Inserire soltanto Embed Code Vimeo"
)


pdf_validator = RegexValidator(
    regex=r'^.+[.]pdf',
    message="Inserire un file in formato .pdf"
)


img_validator = RegexValidator(
    regex=r'^.+[.]jpe?g|.+\.png|.+gif',
    message="Inserire un file in formato .pdf"
)


def percorso_cartella_corsi(instance, filename):
    return 'Corsi/{nome_corso}/{file}'.format(
        nome_corso=instance.nome_corso,
        file=filename)


def percorso_cartella_lezioni(instance, filename):
    return 'Corsi/{nome_corso}/Lezioni/{nome_lezione}/{file}'.format(
        nome_corso=instance.corso_lezione,
        nome_lezione=instance.nome_lezione,
        file=filename)


class Corso(models.Model):
    SEZIONE = (('1', 'Orientamento'), ('2', 'Impresa'), ('3', 'Digitale'))

    docente_corso = models.ForeignKey(User, on_delete=models.CASCADE, related_name="docenti")
    sezione_corso = models.CharField(max_length=1, choices=SEZIONE, blank=True, null=True)
    nome_corso = models.CharField(max_length=80)
    img_corso = models.ImageField(blank=True, null=True, upload_to=percorso_cartella_corsi, verbose_name="Logo")
    descrizione_corso = models.TextField(max_length=2000, blank=True, null=True)
    obiettivi_corso = models.TextField(max_length=4000, blank=True, null=True)
    allegati_corso = models.FileField(blank=True, null=True, upload_to=percorso_cartella_corsi, verbose_name="Scheda Tecnica", validators=[pdf_validator])
    data_corso = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, related_name='followers')

    def __str__(self):
        return self.nome_corso

    def get_absolute_url(self):
        return reverse('finestra_corso', kwargs={"pk": self.pk})

    def get_lessons(self):
        lessons = Lezione.objects.filter(corso_lezione=self.pk)
        return lessons

    class Meta:
        #ordering = ('-created')
        verbose_name = "Corso"
        verbose_name_plural = "Corsi"


class Lezione(models.Model):

    nome_lezione = models.CharField(max_length=80)
    link_lezione = models.CharField(max_length=1000, validators=[embed_validator])
    allegato_lezione = models.FileField(blank=True, null=True, upload_to=percorso_cartella_lezioni)
    corso_lezione = models.ForeignKey(Corso, on_delete=models.CASCADE, related_name="lezioni")
    data_lezione = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    contenuto = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
        'filepdf',
        'linkvideo'
    )})

    def __str__(self):
        return self.nome_lezione

    def get_absolute_url(self):
        return reverse('finestra_lezione', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Lezione"
        verbose_name_plural = "Lezioni"


class Risorsa(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE, related_name="corso")
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    contenuto = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
        'filepdf',
        'linkvideo'
    )})

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Risorsa"
        verbose_name_plural = "Risorse"


class ContenutoBase(models.Model):
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    nome_contenuto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        #verbose_name = "Contenuto"
        #verbose_name_plural = "Contenuti"

    def __str__(self):
        return self.nome_contenuto

class FilePdf(ContenutoBase):
    file = models.FileField(blank=True, null=True, upload_to=percorso_cartella_lezioni)

class LinkVideo(ContenutoBase):
    link = models.URLField(blank=True, null=True, validators=[embed_validator])
