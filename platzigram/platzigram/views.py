"""PLatzigram views"""

from django.http import HttpResponse

# Devuelve un saludo
def hello_world(request):
    return HttpResponse("Hola mundo")