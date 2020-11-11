from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'nombre': 'Molino',
        'user': 'Cesar',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://cdn.pixabay.com/photo/2020/11/04/19/22/windmill-5713337_960_720.jpg',
    },

    {
        'nombre': 'Caballo',
        'user': 'Camilo',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://cdn.pixabay.com/photo/2019/12/26/10/44/horse-4720178_960_720.jpg',
    },
]

def list_post(request):
    contenido = []
    for post in posts:
        contenido.append("""
            <p><strong>{nombre}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src='{picture}'/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(contenido))


