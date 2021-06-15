from django.forms import ModelForm
from django import forms
from pessoa.models import Pessoa, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, DadosProfissional


class LoginForm(ModelForm):
    class Meta:
        model = Pessoa
        widgets = {
            'senha': forms.PasswordInput(),}
        fields = ['email', 'senha']

class PessoaCadastroForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class AgenteSecretariaform(PessoaCadastroForm):
    class Meta:
        model = AgenteSecretaria
        fields = '__all__'


class AdministradorSistemaForm(PessoaCadastroForm):
    class Meta:
        model = AdministradorSistema
        fields = '__all__'


class EnderecoCadastroForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class CargoCadastroForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class DadosProfissionalCadastroForm(ModelForm):
    class Meta:
        model = DadosProfissional
        fields = '__all__'