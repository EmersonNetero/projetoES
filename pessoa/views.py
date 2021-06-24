#from conda.base import context
from django.shortcuts import render
from .models import AgenteSecretaria, AdministradorSistema
from .forms import LoginForm

from .forms import ProfissaoCadastroForm, EnderecoCadastroForm, AgenteSecretariaform, AdministradorSistemaForm, CargoCadastroForm, \
    TipoProcedimentoCadForm, AgendamentoForm, PagamentoForm

from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, "index.html")

###
def login(request):
    data = {}
    data['form'] = LoginForm()
    return render(request, 'login.html', data)

# telas do cargos 
def admSistema(request):
    return render(request, "menuAdmSistema.html")

###
def cadastrarAdministradorSistema(request):
    template = ""
    context = {}
    f = AdministradorSistemaForm()
    if request.method == "POST":
        formAdm = AdministradorSistemaForm(request.POST or None)
        if formAdm.is_valid():
            formAdm.save()
            context['form'] = f
            messages.info(request, "Administrador de Sistema Cadastrado com Sucesso!")
        return render(request, "cadastroPessoa.html", context)
    else:
        formAdm = AdministradorSistemaForm()
    context['form'] = formAdm
    return render(request, "cadastroPessoa.html", context)

###
def cadastrarEndereco(request):
    template = ""
    context = {}
    f = EnderecoCadastroForm()
    if request.method == "POST":
        formEndereco = EnderecoCadastroForm(request.POST)
        if form.is_valid():
            formEndereco.save()
            context['form'] = f
            messages.info(request, "Endereço Cadastrado com Sucesso!")
            return render(request, "cadastroPessoa.html", context)
    else:
        formEndereco = EnderecoCadastroForm(prefix='adr')
    context['form'] = formEndereco

    return render(request, "cadastroPessoa.html", context)

###
def cadastrarCargo(request):
    template = ""
    context = {}
    f = CargoCadastroForm()
    if request.method == "POST":
        formCargo = CargoCadastroForm(request.POST)
        if formCargo.is_valid():
            formCargo.save()
            context['form'] = f
            messages.info(request, "Cargo Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", context)
    else:
        formCargo = CargoCadastroForm()
    context['form'] = formCargo
    return render(request, "cadDiverso.html", context)

###

def cadastrarTipoProcedimento(request):
    template = ""
    context = {}
    f = TipoProcedimentoCadForm
    if request.method == "POST":
        formTipProcedimento = TipoProcedimentoCadForm(request.POST)
        if formTipProcedimento.is_valid():
            formTipProcedimento.save()
            context['form'] = f
            messages.info(request, "Tipo de Procediemnto Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", context)
    else:
        formTipProcedimento = TipoProcedimentoCadForm()
    context['form'] = formTipProcedimento
    return render(request, "cadDiverso.html", context)


###
def cadastrarAgendmentoTeste(request):
    template = ""
    context = {}
    formAgenda = AgendamentoForm(request.POST)
    if formAgenda.is_valid():
        formAgenda.save()
    context['form'] = formAgenda
    return render(request, "agendamento.html", context)

###
def cadastrarPagamentoTeste(request):
    template = ""
    context = {}
    formPag = PagamentoForm(request.POST)
    if formPag.is_valid():
        formPag.save()
    context['form'] = formPag
    return render(request, "agendamento.html", context)