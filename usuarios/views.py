from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Perfil


# Create your views here.

class UsuarioCreate(CreateView):
  template_name = "paginas/form.html"
  form_class = UsuarioForm
  success_url = reverse_lazy('login')

  def form_valid(self, form):
    grupo = get_object_or_404(Group, name="usuarios-filmes")
    url = super().form_valid(form)
    self.object.groups.add(grupo)
    self.object.save()
    Perfil.objects.create(usuario=self.object)
    return url

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['titulo'] = "Cadastro de Usuario"
    context['botao'] = "Cadastrar"
    return context

class PerfilUpdate(UpdateView):
  template_name = "paginas/form.html"
  model = Perfil
  fields = ['apelido', 'nome_completo', 'cpf', 'data_nascimento', 'telefone']
  success_url = reverse_lazy("index")

  def get_object(self, queryset=None):
    self.object = get_object_or_404(Perfil, usuario=self.request.user)
    return self.object

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['titulo'] = "Meus dados pessoais"
    context['botao'] = "Atualizar"
    return context



############# DELETE ###########

class PerfilDelete(DeleteView):
  model = Perfil
  # u = User.objects.get(id = 11)
  # u.delete()
  template_name = 'paginas/form-excluir.html'
  success_url = reverse_lazy('listar-usuario-dados')




############# LISTA ###########


class UsuariosDadosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
  login_url = reverse_lazy('login')
  group_required = u"administrador"
  model = Perfil
  template_name = 'paginas/listas/usuarios-dados.html'

