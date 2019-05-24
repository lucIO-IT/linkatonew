from django import forms
from .models import Corso, Risorsa
from .widgets import emaCSSFileInput, emaCSSImageInput, emaCSSTextInput


class CorsoModelForm(forms.ModelForm):
    SEZIONE = (('0', 'Scegli Sezione'), ('1', 'Orientamento'), ('2', 'Impresa'), ('3', 'Digitale'))

    img_corso = forms.ImageField(widget=emaCSSImageInput())
    allegati_corso = forms.FileField(widget=emaCSSFileInput())
    descrizione_corso = forms.CharField(widget=emaCSSTextInput())
    obiettivi_corso = forms.CharField(widget=emaCSSTextInput())
    sezione_corso = forms.ChoiceField(choices=SEZIONE, widget=forms.Select(
        attrs={
            'class': 'select',
        }
    ))

    class Meta:
        model = Corso
        fields = ['sezione_corso', 'nome_corso', 'descrizione_corso', 'obiettivi_corso', 'allegati_corso', 'img_corso']


class LezioneModelForm(forms.ModelForm):

    class Meta:
        model = Risorsa
        fields = ['nome_lezione', 'link_lezione', 'allegato_lezione']


#LezioneFormset = formset_factory(LezioneModelForm, extra=1)