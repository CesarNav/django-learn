from django.urls import path
#Esto para que el modulo views pueda existir
from platzigram import views


urlpatterns = [
    
    path('hello-world/', views.hello_world),
    path('hi/<str:nombre>/<int:edad>/', views.hi),
    path('num/', views.num)
]
