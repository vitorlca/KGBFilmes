from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ('titulo', 'diretor', 'genero', 'classificacao', 'ano_producao', 'pais_de_origem', 'image')