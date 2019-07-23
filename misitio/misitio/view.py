import datetime
from django.shortcuts import render
from django.http import Http404

def hola(request):
    return HttpResponse("Hola Mundo!")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual':ahora})

def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #assert False
    return render(request, "horas_adelante.html", {'hora_siguiente': dt, 'hora': offset})

