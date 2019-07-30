from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

def contacto(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto',):
            errors.append('Por favor introduce el ausnto.')
        if not request.POST.get('mensaje',):
            errors.append('Por favor introduce un mensaje.')
        if not request.POST.get('email')and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de e-mail valida')
        if not errors:
            send_mail( reques.POST['asunto'], request.POST['mensaje'],
            request.POST.get('email', 'noreplye@example.com'),['siteoner@example.com'],) 
            return HttpResponseRedirect('/contactos/gracias/')
    return render(request, 'formulario-contactos.html', {'errors': errors})
