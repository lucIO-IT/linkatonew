from .models import Corso, Lezione, Risorsa, CorsoProgress
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
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

#*** 1) Dashboard
@login_required
def accountProfileView(request):
    return redirect('list_view', token='dashboard')


@login_required
def listView(request, token):

    if token == 'teachers':
        docenti = []  # User.objects.all()
        for corso in Corso.objects.all():
            docenti.append(corso.docente_corso)
        docenti = list(set(docenti))
        return render(request, 'docenti.html', context={'docenti': docenti})

    elif token == 'docente':
        if "doc" in request.GET:
            query = request.GET.get("doc")
            object_list = Corso.objects.filter(docente_corso=query)
            user = User.objects.get(pk=query)
            context = {"object_list": object_list, "nome_docente": user}
            return render(request, 'platform.html', context)

    elif token == 'user_page':
        object_list = Corso.objects.filter(docente_corso=request.user).all()
        token = 'I Miei Programmi'
        instance = 'mooc_key'
        context = {
            "token": token,
            "object_list": object_list,
            "mooc_key": instance,
        }
        return render(request, 'platform.html', context)

    elif token == 'favorite':
        object_list = Corso.objects.filter(followers=request.user).all()
        token = 'I Miei Preferiti'
        context = {
            "token": token,
            "object_list": object_list,
        }
        return render(request, 'platform.html', context)

    elif token == 'search':
        if "q" in request.GET and "sec" in request.GET:
            querystring = request.GET.get("q")
            token = 'Risultati Ricerca'
            corsi = Corso.objects.filter(nome_corso__icontains=querystring)
            query = request.GET.get("sec")
            if query != "0":
                corsi = corsi.all().filter(sezione_corso__icontains=query)
            if len(querystring) == 0 and query == "0":
                return redirect("/")
            else:
                context = {"object_list": corsi, "token": token}
                return render(request, 'platform.html', context)
    else:
        object_list = Corso.objects.all()
        token = 'Dashboard'

        context = {
            "token": token,
            "object_list": object_list,
        }
        return render(request, 'platform.html', context)
    #if request.user.is_authenticated and not Utente.objects.filter(user=request.user).filter(scuola__isnull=True):
     #   return redirect('registrazione_dati_utente')


@login_required
def cerca(request):
    if "q" in request.GET and "sec" in request.GET:
        querystring = request.GET.get("q")
        token = 'Risultati Ricerca'
        corsi = Corso.objects.filter(nome_corso__icontains=querystring)
        query = request.GET.get("sec")
        if query != "0":
            corsi = corsi.all().filter(sezione_corso__icontains=query)
        if len(querystring) == 0 and query == "0":
            return redirect("/")
        else:
            context = {"object_list": corsi, "token": token}
            return render(request, 'platform.html', context)

#*** 2) Filtri pagine

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


def docente_corsi(request):
    if "doc" in request.GET:
        query = request.GET.get("doc")
        object_list = Corso.objects.filter(docente_corso=query)
        user = User.objects.get(pk=query)
        context = {"object_list": object_list, "nome_docente": user}
        return render(request, 'platform.html', context)


def lista_docenti(request):
    docenti = [] #User.objects.all()
    for corso in Corso.objects.all():
        docenti.append(corso.docente_corso)
    docenti = list(set(docenti))
    return render(request, 'docenti.html', context = {'docenti': docenti})


#*** 3) Salvataggio corso tra i preferiti dell'utente (con ajax)
@login_required
def salvaPreferiti(request, pk):

    corso = get_object_or_404(Corso, pk=pk)
    if request.user in corso.followers.all():
        corso = corso
        corso.followers.remove(request.user)
    else:
        corso = corso
        corso.followers.add(request.user)
        #cerca o crea la progressione corso
        progress, created = CorsoProgress.objects.get_or_create(
            studente =request.user,
            corso =corso
        )
        progress.update_progression()

    return redirect('account_profile')


@login_required
def ajax(request, user, course):
    corso = get_object_or_404(Corso, pk=course)
    if request.user in corso.followers.all():
        corso.followers.remove(user)
    else:
        corso.followers.add(user)
        # cerca o crea la progressione corso
        progress, created = CorsoProgress.objects.get_or_create(
            studente=request.user,
            corso=corso
        )
        progress.update_progression()
    data = {"followers": course}
    return JsonResponse(data)


#*** 4) Detail View
@login_required
def visualizzaCorso(request, pk):
    corso = get_object_or_404(Corso, pk=pk)
    lista_lezioni = Lezione.objects.filter(corso_lezione=corso).order_by('data_lezione')
    prima_lezione = Lezione.objects.filter(corso_lezione=corso).first()
    is_liked = False
    if request.user in corso.followers.all():
        is_liked = True
    context = {"corso": corso, "lista_lezioni": lista_lezioni, "prima_lezione": prima_lezione, "is_liked": is_liked}
    return render(request, "detail.html", context)


@login_required
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
    if request.user in corso_lezione.followers.all():
        progress = CorsoProgress.objects.get(studente=request.user, corso=corso_lezione)
        progress.add_contents(lezione)
        progress.update_progression()

    context = {
        "lezione": lezione,
        "lista_lezioni": lista_lezioni,
        "corso_lezione": corso_lezione,
        "next": next,
        "previous": previous,
        "prev_lista_lezioni": prev_lista_lezioni,
    }
    return render(request, "core/lezione.html", context)


#*** 5) Creazione contenuti
@login_required
def creaCorso(request):

    if request.method == "POST":
        form = CorsoModelForm(request.POST, request.FILES)
        if form.is_valid():
            corso = form.save(commit=False)
            corso.docente_corso = request.user
            corso.save()
            corso.followers.add(request.user)
            progress, created = CorsoProgress.objects.get_or_create(
                studente=request.user,
                corso=corso
            )
            progress.update_progression()
            return redirect('preview_corso', pk=corso.pk)
    else:
        form = CorsoModelForm()
    context = {"form": form}
    return render(request, "crea_corso.html", context)


class FormModificaCorso(UpdateView):
    model = Corso
    template_name = "crea_corso.html"
    form_class = CorsoModelForm

    def get_queryset(self):
        return Corso.objects.filter(docente_corso=self.request.user)

    def get_success_url(self):
        return reverse('preview_corso', kwargs={"pk": self.object.pk})


@login_required
def previewCorso(request, pk):
    corso = get_object_or_404(Corso, pk=pk)

    if request.method == "POST":
        form_lezione = LezioneModelForm(request.POST, request.FILES)
        if form_lezione.is_valid():
            risorsa = form_lezione.save(commit=False)
            #lezione.corso_lezione = corso
            risorsa.save()
            risorsa.create_lezione(corso)
            return redirect('preview_corso', pk=corso.pk)
    else:
        form_lezione = LezioneModelForm()

    lista_lezioni = Lezione.objects.filter(corso_lezione=corso).order_by('data_lezione')
    context = {"corso": corso, "lista_lezioni": lista_lezioni, "form": form_lezione}
    return render(request, "preview.html", context)


@login_required
def eliminaLezione(request, pk):
    lezione = get_object_or_404(Lezione, pk=pk)
    lezione_corso = lezione.corso_lezione
    if request.method == "GET":
        lezione.delete()
        return redirect('preview_corso', pk=lezione_corso.pk)

#Da implementare: ajax form per aggiunta lezioni

def ajax_lesson_form(request):
    form = request.POST['data']
    data = {'fkr': form}
    return JsonResponse(data, safe=False)
