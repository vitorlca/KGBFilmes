from django.urls import path
#importa as views que foram criadas
from .views import IndexView, SobreView

#tem que ser uylpatterns porque é padrão do django
urlpatterns = [
  #Todo path tem endereço, sua_view.as_view() e nome
  #path('endereço', MinhaView.as_view(), name='nome-da-url'), estrura de criação de url
  path('inicio/', IndexView.as_view(), name='index'),
  path('sobre/', SobreView.as_view(), name='sobre'),
]