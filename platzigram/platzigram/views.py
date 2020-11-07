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
    return HttpResponse("Hi")