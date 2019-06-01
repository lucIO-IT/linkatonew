from django import forms
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import FormRegistrazioneUtente, FormDatiUtente, FormDatiScuola, FormAvatar
from django.core.mail import send_mail
from blog.models import Articolo
from .models import Scuola, Utente, Avatar
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.

def indexView(request):
    return redirect('list_view', token='dashboard')
    #return render(request, 'index.html')

"""
import json
def check_scuola(code):
    json_data = open('index/scuole.json')
    json_str = json_data.read()
    data = json.loads(json_str)
    scuole=data["@graph"]
    for var in scuole:
        foo = var["miur:CODICEISTITUTORIFERIMENTO"]
        if foo == code:
            return True
"""

def registrazioneUtente(request):
    if request.method == "POST":
        form = FormRegistrazioneUtente(request.POST)
        form_utente = FormDatiUtente(request.POST, request.user)
        if form.is_valid() and form_utente.is_valid():
            nome = form.cleaned_data["first_name"]
            cognome = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = email
            password = form.cleaned_data["password1"]
            if not User.objects.filter(username=username):
                User.objects.create_user(first_name=nome, last_name=cognome, username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                send_mail(
                    subject='Benvenuto su LINKaTO',
                    message='Ciao ' + nome +
                            '\nLa registrazione a LINKaTO è avvenuta con successo!'
                            '\nDi sgeuito sono riportate le credenziali di accesso:' +
                            '\nUsername: ' + username +
                            '\nPassword: ' + password,
                    from_email='linkato.project@gmail.com',
                    recipient_list=[email]
                    #fail_silently=False
                )
                #utente = form_utente.save(commit=False)
                #utente.user = request.user
                #utente.save()
                gender = form_utente.cleaned_data['genere']
                data = form_utente.cleaned_data['data_nascita']
                scuola = form_utente.cleaned_data['scuola']
                new_user = Utente.objects.create(user=request.user, genere=gender, data_nascita=data, scuola=scuola)
                new_user.save()
                return redirect('avatar')
            else:
                form = FormRegistrazioneUtente()
                form_utente = FormDatiUtente()
                context = {"form": form, "form_utente": form_utente,
                           "user_esiste": 'La mail inserita risulta già associata ad un altro account.\nSi prega di inserire un altro indirizzo di posta'}
                return render(request, "registration/registrazione.html", context)
        else:
            form = FormRegistrazioneUtente()
            form_utente = FormDatiUtente()
            context = {
                "form": form,
                "form_utente": form_utente,
                "user_esiste": 'Attenzione: codice meccanografico inserito non corretto!',
            }
            return render(request, "registration/registrazione.html", context)
    else:
        form = FormRegistrazioneUtente()
        form_utente = FormDatiUtente()
    context = {"form": form, "form_utente": form_utente}
    return render(request, "registration/registrazione.html", context)

"""

def registrazioneUtente(request):
    if request.method == "POST":
        form = FormRegistrazioneUtente(request.POST)
        form_utente = FormDatiUtente(request.POST, request.user)
        if form.is_valid() and form_utente.is_valid():
            utente_scuola = form_utente.cleaned_data["scuola"]
            if check_scuola(utente_scuola) == True:
                nome = form.cleaned_data["first_name"]
                cognome = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                username = email
                password = form.cleaned_data["password1"]
                if not User.objects.filter(username=username):
                    User.objects.create_user(first_name=nome, last_name=cognome, username=username, email=email, password=password)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    send_mail(
                        subject='Benvenuto su LINKaTO',
                        message='Ciao ' + nome +
                                '\nLa registrazione a LINKaTO è avvenuta con successo!'
                                '\nDi sgeuito sono riportate le credenziali di accesso:' +
                                '\nUsername: ' + username +
                                '\nPassword: ' + password,
                        from_email='linkato.project@gmail.com',
                        recipient_list=[email]
                        #fail_silently=False
                    )
                    utente = form_utente.save(commit=False)
                    utente.user = request.user
                    utente.save()
                    return redirect('avatar')
                else:
                    form = FormRegistrazioneUtente()
                    form_utente = FormDatiUtente()
                    context = {"form": form, "form_utente": form_utente,
                               "user_esiste": 'La mail inserita risulta già associata ad un altro account.\nSi prega di inserire un altro indirizzo di posta'}
                    return render(request, "registration/registrazione.html", context)
            else:
                form = FormRegistrazioneUtente()
                form_utente = FormDatiUtente()
                context = {
                    "form": form,
                    "form_utente": form_utente,
                    "user_esiste": 'Attenzione: codice meccanografico inserito non corretto!',
                }
                return render(request, "registration/registrazione.html", context)
    else:
        form = FormRegistrazioneUtente()
        form_utente = FormDatiUtente()
    context = {"form": form, "form_utente": form_utente}
    return render(request, "registration/registrazione.html", context)

"""

def avatar(request):
    if request.method == 'POST':
        form = FormAvatar(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            return redirect('account_profile')
        else:
            form = FormAvatar()
            return render(request, 'registration/avatar.html', context={'form': form})
    else:
        form = FormAvatar()
    return render(request, 'registration/avatar.html', context={'form': form})


class UpdateAvatar(UpdateView):
    model = Avatar
    template_name = "registration/avatar.html"
    form_class = FormAvatar

    def get_queryset(self):
        return Avatar.objects.filter(pk=self.request.user.avatar.pk)

    def get_success_url(self):
        return reverse('account_profile')


def datiScuola(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form_scuola = FormDatiScuola(request.POST)
            if form_scuola.is_valid:
                scuola = form_scuola.save(commit=False)
                utente = Utente.objects.get(user=request.user)
                scuola.codice = utente.scuola
                scuola.save()
                scuola.docenti_scuola.add(request.user)
                return HttpResponseRedirect("../../core/profilo_utente/")
        else:
            form_scuola = FormDatiScuola()
            context = {"form_scuola": form_scuola}
            return render(request, 'registration/dati.html', context)
    else:
        return redirect('registrazione')


def cercaHome(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        print(querystring)
        if len(querystring) == 0:
            return redirect('/')
        articoli = Articolo.objects.filter(title__icontains=querystring)
        context = {"articoli": articoli}
        return render(request, 'risultati_ricerca.html', context)

"""
import json
from django.http import JsonResponse
from django.http import HttpResponse
def prova_json_scuole(request, code):
    json_data = open('index/scuole.json')
    json_str = json_data.read()
    data = json.loads(json_str)
    scuole=data["@graph"]
    list=[]
    scuola = ''
    grado = ''
    comune = ''
    provincia = ''
    for var in scuole:
        foo = var["miur:CODICEISTITUTORIFERIMENTO"]
        #print(foo)
        list.append(foo)
        if foo == code:
            scuola = var['miur:DENOMINAZIONEISTITUTORIFERIMENTO']
            grado = var['miur:DESCRIZIONETIPOLOGIAGRADOISTRUZIONESCUOLA']
            #indirizzo = var['miur:INDIRIZZOSCUOLA']
            comune = var['miur:DESCRIZIONECOMUNE']
            provincia = var['miur:PROVINCIA']
            #regione = var['miur:REGIONE']
            #email = var['miur:INDIRIZZOEMAILSCUOLA']
            #pec = var['miur:INDIRIZZOPECSCUOLA']
            #sitoweb = var['miur:SITOWEBSCUOLA']

    return HttpResponse(scuola + grado + comune + provincia)



    #return JsonResponse(list, safe=False)
"""


