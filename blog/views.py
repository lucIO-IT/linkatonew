from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from django.views.generic.list import ListView
from .models import Articolo
from core.models import Corso
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.

""" La prima funzione permette di visionare i dettagli dell'articolo """

def articoloView(request, title):
    articolo = get_object_or_404(Articolo, title=title)
    context = {'articolo': articolo}
    return render(request, 'pagina_articolo.html', context)


class ArticoloList(ListView):
    model = Articolo
    template_name = 'lista_articoli.html'
    paginate_by = 9


def visualizzaChiSiamo(request):
    sezione = Articolo.objects.filter(sezione=1)
    context = {"sezione": sezione}

    return render(request, "pagina_articolo.html", context)


def visualizzaPerAziende(request):
    sezione = Articolo.objects.filter(sezione=2)
    context = {"sezione": sezione}

    return render(request, "pagina_articolo.html", context)


def visualizzaTopNew(request):
    sezione = Articolo.objects.filter(sezione=3)
    object_list = Corso.objects.all()
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    object_list = paginator.get_page(page)

    context = {"sezione": sezione, "object_list": object_list}
    return render(request, "pagina_articolo.html", context)


def visualizzaCardSx(request):
    sezione = Articolo.objects.filter(sezione=4)
    context = {"sezione": sezione}

    return render(request, "pagina_articolo.html", context)


def visualizzaCardCc(request):
    sezione = Articolo.objects.filter(sezione=5)
    context = {"sezione": sezione}

    return render(request, "pagina_articolo.html", context)


def visualizzaCardDx(request):
    sezione = Articolo.objects.filter(sezione=6)
    context = {"sezione": sezione}

    return render(request, "pagina_articolo.html", context)