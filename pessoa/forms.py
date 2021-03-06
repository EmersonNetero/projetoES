from django.forms import ModelForm
from django import forms
from pessoa.models import Profissao, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, Procedimento, \
    TipoProcedimento, Pagamento, Paciente, AgenteSaude, Agendamento
from django.utils import timezone
import datetime
from importlib import import_module

class LoginForm(ModelForm):
    class Meta:
        model = Profissao
        widgets = {
            'senha': forms.PasswordInput(),}
        fields = ['email', 'senha']


class ProfissaoForm(ModelForm):
    class Meta:
        model = Profissao
        exclude = ('fk_endereco',)


class AgenteSecretariaForm(ProfissaoForm):
    class Meta:
        model = AgenteSecretaria
        exclude = ('fk_endereco',)


class AgenteSaudeForm(ProfissaoForm):
    class Meta:
        model = AgenteSaude
        exclude = ('fk_endereco',)


class AdministradorSistemaForm(ProfissaoForm):
    class Meta:
        model = AdministradorSistema
        exclude = ('fk_endereco',)


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class TipoProcedimentoForm(ModelForm):
    class Meta:
        model = TipoProcedimento
        fields = '__all__'


class AgendamentoForm(ModelForm):
    data_agendamento = forms.DateField(localize=False,
                                      widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
                                      initial=datetime.datetime.now())
    tipo_agendamento = forms.CharField(widget=forms.TextInput())
    observacao = forms.CharField(max_length=300, required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 4}), label='Observação')
    pago = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'size': 20}))
    confirmado = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'size': 20}))

    class Meta:
        model = Agendamento
        fields = '__all__'


class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = '__all__'


class PacienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(localize=False,
        widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),initial=datetime.datetime.now())

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('fk_endereco',)


class ProcedimentoForm(ModelForm):
    class Meta:
        model = Procedimento
        fields = '__all__'




