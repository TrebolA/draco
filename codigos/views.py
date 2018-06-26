from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from .forms import CodigoForm
from django.shortcuts import redirect
from codigos.models import Codigo
from django.http import HttpResponse
import random
import csv


def codigo_list(request):
        return render(request, 'CODIGOS INCUBUS.txt')


def home(request):
    if request.method == "POST":
        form = CodigoForm(request.POST)
        if form.is_valid():
            inscrito = form.save(commit=False)
            listCodigos = []
            numAlea = random.randrange(1000)
            f = open('codigos.txt')
            linea = f.readline()
            while linea != "":
                listCodigos.append(linea)
                linea = f.readline()
            darCodigo = listCodigos.pop(numAlea)
            inscrito.codigo = darCodigo
            inscrito.save()

            subject = 'Codigo de preventa Queens Of The Stone Age'
            text_content = 'Tu codigo para la preventa de Queens Of The Stone Age es: '+inscrito.codigo
            html_content = '<style type="text/css"> table{background-color: #f8faef; background-image: url(https://gallery.mailchimp.com/1a1976824fdbd12281545222a/images/7414e094-171c-4cae-8ce6-7acb2bb9848e.png); background-size: 50%; background-repeat: no-repeat;} .gracias{padding-left: 60%; margin: 2%;} #codigo{padding: 3%; padding-left: 77%; font-size: 250%; font-family: helvetica;} #album{padding-left: 25%; padding-bottom: 4%;} #footer{width: 100%;}</style><table><tr><td><img src="https://gallery.mailchimp.com/1a1976824fdbd12281545222a/images/25f763c8-6bc2-4ea4-be4d-8dfb1fb59c23.png" class="gracias"></td></tr><tr><td id="codigo">'+inscrito.codigo+'</td></tr><tr><td><img src="https://gallery.mailchimp.com/1a1976824fdbd12281545222a/images/0e92fc6f-0719-4e96-82e0-7948f9f5c02d.png" class="gracias"></td></tr><tr><td><img src="https://gallery.mailchimp.com/1a1976824fdbd12281545222a/images/8480f270-e459-4917-8697-5aadb5676428.png" id="album"></td></tr><tr><td><img src="https://gallery.mailchimp.com/1a1976824fdbd12281545222a/images/690abab0-0c16-43cb-8749-515a9631f8db.png" id="footer"></td></tr></table>'
            from_email = '"Paramo Presenta" <info@paramopresenta.com>'
            to = inscrito.correo
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            f1 = open("codigos.txt", 'w')
            for x in listCodigos:
                f1.write(x)
            f1.close()
            f.close()
            return redirect('gracias')
    else:
        form = CodigoForm()
    return render(request, 'home.html', {'form': form})


def gracias(request):
    return render(request, 'gracias.html')


def exportCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DB Draco.csv"'

    writer = csv.writer(response)

    for x in Codigo.objects.all():
        writer.writerow([x.nombre, x.apellido, x.correo, x.celular])

    return response
