from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MailForm

# Create your views here.


def invioMail(request):
    if request.method == 'GET':
        form = MailForm()
    else:
        form = MailForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mail = form.cleaned_data['mail']
            oggetto = form.cleaned_data['oggetto']
            testo = form.cleaned_data['testo']
            send_mail(
                subject=oggetto,
                message='da' + nome + '\n' + testo,
                from_email=mail,
                recipient_list=['linkato.project@gmail.com']
            )
            #except BadHeaderError:
            #    return HttpResponse('Invalid header found.')
            return redirect('mail_done')

    return render(request, 'mail_form.html', {'form': form})

def mailInviata(request):
    return render(request, 'mail_done.html')

