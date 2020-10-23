from django.shortcuts import render

# Importa o TemplateView para criar paginas simples
from django.views.generic import TemplateView

# Create your views here.

# A classe PaginaInicial "estends" TemplateView
class IndexView(TemplateView):
  # Toda classe filha do TemplateView precisa do
  # atributo abaixo para definir um template a ser renderizado
  template_name = 'paginas/index.html'

class SobreView(TemplateView):
  template_name = 'paginas/sobre.html'

