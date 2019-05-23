from django import forms
from .models import Corso, Risorsa


class CorsoModelForm(forms.ModelForm):

    allegati_corso = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Corso
        fields = ['sezione_corso', 'nome_corso', 'descrizione_corso', 'obiettivi_corso', 'allegati_corso', 'img_corso']


class LezioneModelForm(forms.ModelForm):

    class Meta:
        model = Risorsa
        fields = ['nome_lezione', 'link_lezione', 'allegato_lezione']


#LezioneFormset = formset_factory(LezioneModelForm, extra=1)