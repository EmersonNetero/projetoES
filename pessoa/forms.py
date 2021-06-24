from django.forms import ModelForm
from django import forms
from pessoa.models import Profissao, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, Procedimento, \
    TipoProcedimento, Pagamento, Paciente, AgenteSaude, Agendamento


class LoginForm(ModelForm):
    class Meta:
        model = Profissao
        widgets = {
            'senha': forms.PasswordInput(),}
        fields = ['email', 'senha']

class ProfissaoCadastroForm(ModelForm):
    class Meta:
        model = Profissao
        fields = '__all__'


class AgenteSecretariaform(ProfissaoCadastroForm):
    class Meta:
        model = AgenteSecretaria
        fields = '__all__'


class AdministradorSistemaForm(ProfissaoCadastroForm):
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

class TipoProcedimentoCadForm(ModelForm):
    class Meta:
        model = TipoProcedimento
        fields = '__all__'


class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'

