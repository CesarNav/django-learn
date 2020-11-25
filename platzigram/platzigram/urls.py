from django.urls import path
from django.contrib import admin
#Esto para que el modulo views pueda existir
from platzigram import views as local_views
from post import views as post_views


urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('hello-world/', local_views.hello_world),
    path('hi/<str:nombre>/<int:edad>/', local_views.hi),
    path('num/', local_views.num),

    path('post/', post_views.list_post),

]
