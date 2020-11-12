#from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

#usando render
def list_post(request):
    return render(request, 'feed.html', {'posts': posts})

#usando httpresponse
#def list_post(request):
    #contenido = []
    #for post in posts:
        #contenido.append("""
            #<p><strong>{nombre}</strong></p>
            #<p><small>{user} - <i>{timestamp}</i></small></p>
            #<figure><img src='{picture}'/></figure>
        #""".format(**post))
    #return HttpResponse('<br>'.join(contenido))
