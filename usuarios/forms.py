from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
  email = forms.EmailField(max_length=100)

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


# class UserDeleteForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.