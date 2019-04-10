from django import forms
from django.forms import TextInput
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Utente, Scuola

class FormRegistrazioneUtente(UserCreationForm):
    #username = forms.CharField(required=False)
    email = forms.CharField(required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    """""""""""""""""

    def checkUsername(self):
        username = self.cleaned_data['email']
        if User.objects.filter(username=username).all():
            raise forms.ValidationError("Esiste già un utente iscritto con questa email.\n"
                                            "Si prega di accedere con un altro indirizzo di posta")
        return username
        
    """""""""""""""

class FormDatiScuola(forms.ModelForm):
    class Meta:
        model = Scuola
        fields = ['nome_scuola', 'regione', 'provincia']

class FormDatiUtente(forms.ModelForm):
    class Meta:
        model = Utente
        widgets = {
            'scuola': TextInput(attrs={'max_lenght': '8'})
        }
        fields = ['genere', 'data_nascita', 'scuola']