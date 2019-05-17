from .models import Corso, Lezione
from .forms import CorsoModelForm, LezioneModelForm
from django.contrib.auth.models import User
from index.models import Utente
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from datetime import datetime
from django.forms import modelformset_factory
from django.db.models import Q


# Create your views here.

#*** 1) Dashboard

def accountProfileView(request):
    if request.user.is_authenticated:
        preferiti = Corso.objects.filter(followers=request.user)
        preferiti_prev = Corso.objects.filter(followers=request.user)[:3]
        miei_corsi = Corso.objects.filter(docente_corso=request.user)
        miei_corsi_prev = Corso.objects.filter(docente_corso=request.user)[:3]
        popolari = Corso.objects.annotate(num_followers=Count('followers')).order_by('-num_followers')[:3]
        object_list = Corso.objects.all()
        context = {
            "popolari": popolari,
            "miei_corsi": miei_corsi,
            "miei_corsi_prev": miei_corsi_prev,
            "preferiti": preferiti,
            "preferiti_prev": preferiti_prev,
            "object_list": object_list
        }
        #return render(request, 'core/account_profile.html', context)
        return render(request, 'platform.html', context)
    if request.user.is_anonymous:
        return redirect('login')
    #if request.user.is_authenticated and not Utente.objects.filter(user=request.user).filter(scuola__isnull=True):
     #   return redirect('registrazione_dati_utente')


class EliminaAccount(DeleteView):
    model = User
    template_name = "core/delete_account.html"

    def get_success_url(self):
        return reverse('homepage')


def cerca(request):
    if "q" in request.GET and "sec" in request.GET:
        querystring = request.GET.get("q")
        corsi = Corso.objects.filter(nome_corso__icontains=querystring)
        query = request.GET.get("sec")
        if query != "0":
            corsi = corsi.all().filter(sezione_corso__icontains=query)
        if len(querystring) == 0 and query == "0":
            return redirect("/")
        else:
            context = {"object_list": corsi}
            return render(request, 'platform.html', context)


def docente_corsi(request):
    if "doc" in request.GET:
        query = request.GET.get("doc")
        corsi = Corso.objects.filter(docente_corso=query)
        user = User.objects.get(pk=query)
        context = {"object_list": corsi, "nome_docente": user}
        return render(request, 'platform.html', context)


def lista_docenti(request):
    docenti = [] #User.objects.all()
    for corso in Corso.objects.all():
        docenti.append(corso.docente_corso)
    docenti = list(set(docenti))
    return render(request, 'docenti.html', context = {'docenti': docenti})


#*** 2) Filtri elenco Corsi (List View)

def listaCorsi(request):
    #object_list = Corso.objects.annotate(num_followers=Count('followers')).exclude(followers=request.user).exclude(docente_corso=request.user).order_by('-num_followers')
    corsi_list = Corso.objects.all()
    user = request.user
    paginator = Paginator(corsi_list, 8)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)
    popolari = Corso.objects.annotate(num_followers=Count('followers')).order_by('-num_followers')[:4]

    context = {"object_list": object_list, "user": user, "popolari": popolari}
    return render(request, 'core/lista_corsi.html', context)


def filtraCorsoOrientamento(request):
    sezione = Corso.objects.filter(sezione_corso=1).exclude(followers=request.user).exclude(docente_corso=request.user)
    paginator = Paginator(sezione, 4)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    context = {"object_list": object_list}
    return render(request, "core/lista_corsi.html", context)


def filtraCorsoImpresa(request):
   sezione = Corso.objects.filter(sezione_corso=2).exclude(followers=request.user).exclude(docente_corso=request.user)
   paginator = Paginator(sezione, 4)
   page = request.GET.get('page')
   object_list = paginator.get_page(page)

   context = {"object_list": object_list}
   return render(request, "core/lista_corsi.html", context)


def filtraCorsoDigitale(request):
    sezione = Corso.objects.filter(sezione_corso=3).exclude(followers=request.user).exclude(docente_corso=request.user)
    paginator = Paginator(sezione, 4)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    context = {"object_list": object_list}
    return render(request, "core/lista_corsi.html", context)

def filtraCorsoPreferiti(request):
    utente = request.user
    preferiti = Corso.objects.filter(followers=utente)
    object_list = preferiti.all()
    context = {"object_list": object_list}
    return render(request, "platform.html", context)


def visualizzaMieiMooc(request):
    autore = Corso.objects.filter(docente_corso=request.user)
    instance = 'mooc_key'
    object_list = autore.all()
    context = {"object_list": object_list, "mooc_key": instance}
    return render(request, "platform.html", context)


#*** 3) Preferiti Func

def controllaUserFollower(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    if request.user in corso.followers.all():
        follower_user = True
    else:
        follower_user = False
    return follower_user


def salvaPreferiti(request, pk):

    corso = get_object_or_404(Corso, pk=pk)
    #is_liked = False
    #if request.method == 'GET':
    if request.user in corso.followers.all():
        corso = corso
        corso.followers.remove(request.user)
        #is_liked = False
        #return redirect('account_profile')
    else:
        corso = corso
        corso.followers.add(request.user)
        #is_liked = True
    return redirect('account_profile')


#*** 4) Detail View

def visualizzaCorso(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    lista_lezioni = Lezione.objects.filter(corso_lezione=corso).order_by('data_lezione')
    prima_lezione = Lezione.objects.filter(corso_lezione=corso).first()
    is_liked = False
    if request.user in corso.followers.all():
        is_liked = True
    context = {"corso": corso, "lista_lezioni": lista_lezioni, "prima_lezione": prima_lezione, "is_liked": is_liked}
    return render(request, "detail.html", context)


def visualizzaLezione(request, pk):
    lezione = get_object_or_404(Lezione, pk=pk)
    corso_lezione = lezione.corso_lezione
    lista_lezioni = Lezione.objects.filter(corso_lezione=corso_lezione).order_by('data_lezione')
    prev_lista_lezioni = Lezione.objects.filter(corso_lezione=corso_lezione).order_by('-data_lezione')
    next = lista_lezioni[0]
    previous = prev_lista_lezioni[0]

    for i in lista_lezioni:
        if int(i.pk) <= pk:
            continue
        else:
            next = i
            break

    for x in prev_lista_lezioni:
        if int(x.pk) >= pk:
            continue
        else:
            previous = x
            break

    context = {
        "lezione": lezione,
        "lista_lezioni": lista_lezioni,
        "corso_lezione": corso_lezione,
        "next": next,
        "previous": previous,
        "prev_lista_lezioni": prev_lista_lezioni,

    }
    return render(request, "core/lezione.html", context)


#*** 5) CRUD Content

def creaCorso(request):

    if request.method == "POST":
        form = CorsoModelForm(request.POST, request.FILES)
        if form.is_valid():
            corso = form.save(commit=False)
            corso.docente_corso = request.user
            corso.save()
            #corso.followers.add(request.user)
            return redirect('preview_corso', pk=corso.pk)
    else:
        form = CorsoModelForm()
    context = {"form": form}
    return render(request, "crea_corso.html", context)


class FormModificaCorso(UpdateView):
    model = Corso
    fields = ['sezione_corso', 'nome_corso', 'img_corso', 'allegati_corso', 'descrizione_corso', 'obiettivi_corso']
    template_name = "crea_corso.html"

    def get_success_url(self):
        return reverse('preview_corso', kwargs={"pk": self.object.pk})


def previewCorso(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    form = CorsoModelForm(request.POST or None, request.FILES, instance=corso)

    #NB: il form per modificare il corso è stato inserito nella modal
    if request.method == "POST" and 'form_modifica_corso' in request.POST:

        if form.is_valid():
            corso = form.save(commit=False)
            corso.docente_corso = request.user
            corso.followers.add(request.user)
            corso.data_corso = datetime.now()
            corso.save()
            return redirect('preview_corso', pk=corso.pk)
    else:
        form = CorsoModelForm(instance=corso)

    lista_lezioni = Lezione.objects.filter(corso_lezione=corso).order_by('data_lezione')

    if request.method == "POST" and 'form_lezione' in request.POST:
        form_lezione = LezioneModelForm(request.POST, request.FILES)
        if form_lezione.is_valid():
            lezione = form_lezione.save(commit=False)
            lezione.corso_lezione = corso
            lezione.save()
            return redirect('preview_corso', pk=corso.pk)
    else:
        form_lezione = LezioneModelForm()

    context = {"corso": corso, "lista_lezioni": lista_lezioni, "form": form, "form_lezione": form_lezione}
    return render(request, "preview.html", context)


def eliminaLezione(request, pk):
    lezione = get_object_or_404(Lezione, pk=pk)
    lezione_corso = lezione.corso_lezione
    if request.method == "GET":
        lezione.delete()
        return redirect('preview_corso', pk=lezione_corso.pk)


############Non più utilizzati#############

class CorsiList(ListView):
    queryset = Corso.objects.all()
    template_name = 'core/lista_corsi.html'
    paginate_by = 3


def eliminaCorso(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    if request.method == "GET":
        corso.delete()
        return redirect('miei_mooc')


def cancellaPreferiti(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    if request.method == 'GET' and request.user in corso.followers.all():
        corso = corso
        corso.followers.remove(request.user)
    # return redirect('corsi_preferiti')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

###########################################