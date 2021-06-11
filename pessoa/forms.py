from django.forms import ModelForm
from pessoa.models import Pessoa


class LoginForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email', 'senha']