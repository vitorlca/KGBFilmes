from django.db import models

# Create your models here.

class Image(models.Model):
  titulo = models.CharField(max_length=100)
  diretor = models.CharField(max_length=100, null=True, blank=True)
  genero = models.CharField(max_length=100, null=True, blank=True)
  classificacao = models.CharField(max_length=100, null=True, blank=True)
  ano_producao = models.CharField(max_length=100, null=True, blank=True)
  pais_de_origem = models.CharField(max_length=100, null=True, blank=True)
  image = models.ImageField(upload_to='images/', null=True, blank=True)

  def __str__(self):
    return self.titulo
