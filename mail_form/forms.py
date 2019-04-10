from django import forms


class MailForm(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    mail = forms.EmailField(required=True)
    oggetto = forms.CharField(max_length=200, required=True)
    testo = forms.CharField(max_length=4000, widget=forms.Textarea, required=True)