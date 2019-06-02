from django import forms
from django.forms import TextInput
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Utente, Scuola, Avatar
import json

class FormRegistrazioneUtente(UserCreationForm):
    #username = forms.CharField(required=False)
    email = forms.CharField(required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("email")
        if User.objects.filter(username=username).all():
            raise forms.ValidationError("Esiste già un utente iscritto con questa email.\n"
                                            "Si prega di accedere con un altro indirizzo di posta")
        return username

class FormDatiScuola(forms.ModelForm):
    class Meta:
        model = Scuola
        fields = ['nome_scuola', 'regione', 'provincia']

class FormDatiUtente(forms.ModelForm):
    class Meta:
        model = Utente
        widgets = {
            'scuola': TextInput(attrs={'max_lenght': '16'}),
            'data_nascita': forms.DateInput(attrs={'placeholder': 'gg/mm/aaaa'}),
        }
        fields = ['genere', 'data_nascita', 'scuola']

    def clean_scuola(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("scuola")
        json_data = open('index/scuole.json')
        json_str = json_data.read()
        data = json.loads(json_str)
        scuole = data["@graph"]
        list = []
        for var in scuole:
            list.append(var["miur:CODICEISTITUTORIFERIMENTO"])

        if code not in list:
            raise forms.ValidationError("Attenzione: il codice meccanografico inserito non esiste \n"
                                        "Verificare che i valori inseriti siano corretti e quindi riprovare")
        return code


class FormAvatar(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['picture']