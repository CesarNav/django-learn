"""PLatzigram views"""

from django.http import HttpResponse
#Utilidades
from datetime import datetime
import json


def hello_world(request):
    #Devuelve la hora del servidor (%b Meses %dth Dias, %Y años -%H:%M horas y minutos)
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    # Devuelve un saludo
    return HttpResponse("Hola mundo, la hora de servidor es {now}".format(
        now=now
    ))

def hi(request, nombre, edad):
    #Devuelve un saludo
    if edad < 18:
        message = "Lo sentimos {}, no eres bienvenido aqui".format(nombre)
    else:
        message = "Hola {}, Puedes ingresar".format(nombre)
    return HttpResponse(message)

def num(request):
    #Devuelve un lista ordenada de numeros
    numbers = [int (i) for i in request.GET['numeros'].split(',')]
    num_ord = sorted(numbers)
    data = {
        'status' : 'ok',
        'numbers': num_ord,
        'messsage': 'Integers sorted successfully'
    }
    #import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data), content_type='application/json')