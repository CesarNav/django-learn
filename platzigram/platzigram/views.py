"""PLatzigram views"""

from django.http import HttpResponse
#Utilidades
from datetime import datetime

def hello_world(request):
    #Devuelve la hora del servidor (%b Meses %dth Dias, %Y años -%H:%M horas y minutos)
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    # Devuelve un saludo
    return HttpResponse("Hola mundo, la hora de servidor es {now}".format(
        now=now
    ))

def hi(request):
    #pdb es una utilidad de python que pone un debugger en consola cada que llega al codigo
    return HttpResponse("Hola")

def num(request):
    numbers = [int (i) for i in request.GET['numeros'].split(',')]
    num_ord = sorted(numbers)
    #import pdb; pdb.set_trace()
    return HttpResponse(str(numbers), content_type='application/json')