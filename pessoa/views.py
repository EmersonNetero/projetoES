#from conda.base import context
from django.shortcuts import render
from .models import AgenteSecretaria, AdministradorSistema
from .forms import LoginForm

from .forms import PessoaCadastroForm, EnderecoCadastroForm, AgenteSecretariaform, AdministradorSistemaForm, \
    CargoCadastroForm, DadosProfissionalCadastroForm

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
def cadastrarPessoa(request):
    template = ""
    context = {}
    form = PessoaCadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "cadastroPeople.html", context)

###
def cadastrarAgenteSecretaria(request):
    template = ""
    context = {}
    f = AgenteSecretariaform()
    if request.method == "POST":
        form = AgenteSecretariaform(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = f
            messages.info(request, "Agente de Secretaria Cadastrado com Sucesso!")
            return render(request, "cadastroSecretary.html", context)
    else:
        form = AgenteSecretariaform()
    context['form'] = form
    return render(request, "cadastroSecretary.html", context)


def listaAgenteSecretaria(request):
    template = ""
    context = {}
    context["lista"] = AgenteSecretaria.objects.all()
    return render(request, "listaSecretaria.html", context)


def detalheAgenteSecretaria(request, id):
    template = ""
    context = {}
    context['lista'] = AgenteSecretaria.objects.get(pk_agente_secretaria = id)
    return render(request, "listaSecretariaID.html", context)

###
def cadastrarAdministradorSistema(request):
    template = ""
    context = {}
    f = AdministradorSistemaForm()
    if request.method == "POST":
        form = AdministradorSistemaForm(request.POST or None)
        if form.is_valid():
            form.save()
            context['form'] = f
            messages.info(request, "Administrador de Sistema Cadastrado com Sucesso!")
        return render(request, "cadastroSecretary.html", context)
    else:
        form = AdministradorSistemaForm()
    context['form'] = form
    return render(request, "cadastroSecretary.html", context)


def listaAdministradorSistema(request):
    template = ""
    context = {}
    context["lista"] = AdministradorSistema.objects.all()
    return render(request, "listaSecretaria.html", context)


def detalheAdministradorSistema(request, id):
    template = ""
    context = {}
    context['lista'] = AdministradorSistema.objects.get(pk_adm_sistema = id)
    return render(request, "listaSecretariaID.html", context)

###
def cadastrarEndereco(request):
    template = ""
    context = {}
    f = EnderecoCadastroForm()
    if request.method == "POST":
        form = EnderecoCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = f
            messages.info(request, "Endereço Cadastrado com Sucesso!")
            return render(request, "cadastroAddress.html", context)
    else:
        form = EnderecoCadastroForm()
    context['form'] = form
    return render(request, "cadastroAddress.html", context)

###
def cadastrarCargo(request):
    template = ""
    context = {}
    f = CargoCadastroForm()
    if request.method == "POST":
        form = CargoCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = f
            messages.info(request, "Cargo Cadastrado com Sucesso!")
            return render(request, "cadastroAddress.html", context)
    else:
        form = CargoCadastroForm()
    context['form'] = form
    return render(request, "cadastroAddress.html", context)

###
def cadastrarDadosProfissional(request):
    template = ""
    context = {}
    f = DadosProfissionalCadastroForm()
    if request.method == "POST":
        form = DadosProfissionalCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = f
            messages.info(request, "Dados Profissionais Cadastrado com Sucesso!")
            return render(request, "cadastroAddress.html", context)
    else:
        form = DadosProfissionalCadastroForm()
    context['form'] = form
    return render(request, "cadastroAddress.html", context)
