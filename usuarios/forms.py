from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil
from django.forms.widgets import DateInput

class UsuarioForm(UserCreationForm):
  email = forms.EmailField(max_length=100)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


# class UserDeleteForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.



# FORMULÁRIO DO USUÁRIO
class FormUsuario(forms.ModelForm):

  data_nascimento = forms.DateField(label=u'Data de Nascimento *',
  widget=DateInput(format='%d/%m/%Y', attrs={'maxlength':'10'}), input_formats=['%d/%m/%Y'], )
  class Meta:
    model = Perfil
    fields = ['apelido', 'nome_completo', 'cpf', 'data_nascimento', 'telefone']