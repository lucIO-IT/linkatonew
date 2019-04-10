from django.db import models
from django.utils import timezone

# Create your models here.

class Articolo(models.Model):

    SEZIONE = (
        ('1', 'Chi siamo'),
        ('2', 'Per le aziende'),
        ('3', 'top_new'),
        ('4', 'card_sx'),
        ('5', 'card_cc'),
        ('6', 'card_dx')
    )

    sezione = models.CharField(max_length=1, choices=SEZIONE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def pubblicazione(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"