#from conda.base import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import AgenteSecretaria, AdministradorSistema
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaForm, AgenteSaudeForm, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm
from django.contrib import messages


###

def cria_user_django(info):
    user = User.objects.create_user(info['email'], info['email'], info['senha'])
    user.first_name = info['nome']
    user.last_name = info['nome'] + 'sobrenome'
    user.save()
###

def login_user(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('admSistema')
        else:
            messages.error(request, "email ou senha errado!!")
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


# Create your views here.
def home(request):
	return render(request, "principal.html")

###


# telas do cargos 
def admSistema(request):
    return render(request, "menuAdmSistema.html")

###
def cadastrarCargo(request):
    context = {}
    f = CargoForm()
    head = 1
    if request.method == "POST":
        formCargo = CargoForm(request.POST)
        if formCargo.is_valid():
            formCargo.save()
            context['form'] = f
            messages.info(request, "Cargo Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", {'formG': f, 'head': head})
    else:
        formCargo = CargoForm()
    context['form'] = formCargo
    return render(request, "cadDiverso.html", {'formG': formCargo, 'head': head})

###

def cadastrarTipoProcedimento(request):
    context = {}
    f = TipoProcedimentoForm
    head = 2
    if request.method == "POST":
        formTipProcedimento = TipoProcedimentoForm(request.POST)
        if formTipProcedimento.is_valid():
            formTipProcedimento.save()
            context['form'] = f
            messages.info(request, "Tipo de Procediemnto Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", {'formTp': f, 'head': head})
    else:
        formTipProcedimento = TipoProcedimentoForm()
    context['form'] = formTipProcedimento
    return render(request, "cadDiverso.html", {'formTp': formTipProcedimento, 'head': head})


###
def cadastrarPaciente(request):
    context = {}
    if request.method == 'POST':
        formP = PacienteForm(request.POST)
        formE = EnderecoForm(request.POST)
        if formP.is_valid() and formE.is_valid():
            endereco = formE.save()
            paciente = formP.save(commit=False)
            paciente.fk_endereco = endereco
            paciente.save()
            messages.info(request, "Paciente Cadastrado com Sucesso!")
            return HttpResponseRedirect("/cadastrarPaciente")
    else:
        formP = PacienteForm()
        formE = EnderecoForm()
    return render(request, "paciente.html", {'formP': formP, 'formE': formE})


###
def cadastraAgntSecretaria(request):
    if request.method == "POST":
        formS = AgenteSecretariaForm(request.POST)
        formE = EnderecoForm(request.POST)
        if formS.is_valid() and formE.is_valid():
            cria_user_django(request.POST)
            endereco = formE.save()
            agntSecretaria = formS.save(commit=False)
            agntSecretaria.fk_endereco = endereco
            agntSecretaria.save()
            messages.info(request, "Agente de secretaria cadastrado com sucesso")
            return HttpResponseRedirect("/cadastrarAgntSecretaria")
    else:
        formS = AgenteSecretariaForm()
        formE = EnderecoForm()
    return render(request, "agntSecretaria.html", {'formS': formS, 'formE': formE})

###
def cadastraAgntSaude(request):
    if request.method == "POST":
        saude = AgenteSaudeForm(request.POST)
        formE = EnderecoForm(request.POST)
        if saude.is_valid() and formE.is_valid():
            cria_user_django(request.POST)
            endereco = formE.save()
            agntSaude = saude.save(commit=False)
            agntSaude.fk_endereco = endereco
            agntSaude.save()
            messages.info(request, "Agente de Saúde cadastrado com sucesso")
            return HttpResponseRedirect("/cadastrarAgntSaude")
    else:
        saude = AgenteSaudeForm()
        formE = EnderecoForm()
    return render(request, "agntSaude.html", {'saude': saude, 'formE': formE})

###
def cadastrarEndereco(request):
    context = {}
    f = EnderecoForm
    head = 3
    if request.method == "POST":
        formEndereco = EnderecoForm(request.POST)
        if formEndereco.is_valid():
            formEndereco.save()
            context['form'] = f
            messages.info(request, "Endereço Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", {'formEn': f, 'head': head})
    else:
        formEndereco = EnderecoForm()
    context['form'] = formEndereco
    return render(request, "cadDiverso.html", {'formEn': formEndereco, 'head': head})


###
def cadAdmSistema(request):
    if request.method == "POST":
        adm = AdministradorSistemaForm(request.POST)
        formE = EnderecoForm(request.POST)
        if adm.is_valid() and formE.is_valid():
            cria_user_django(request.POST)
            endereco = formE.save()
            adm2 = adm.save(commit=False)
            adm2.fk_endereco = endereco
            adm2.save()
            messages.info(request, "Administrador do Sistema cadastrado com sucesso")
            return HttpResponseRedirect("/cadAdmSistema")
    else:
        adm = AdministradorSistemaForm()
        formE = EnderecoForm()
    return render(request, "cadastroPessoa.html", {'adm': adm, 'formE': formE})


def agendarConsultas(request):
    context = {}
    f = AgendamentoForm()
    if request.method == 'POST':
        formAgenda = AgendamentoForm(request.POST)
        if formAgenda.is_valid():
            formAgenda.save()
            context['formAgenda'] = f
            messages.info(request, "Agendamento cadastrado com sucesso!")
            return HttpResponseRedirect("/agendamento")
    else:
        formAgenda = AgendamentoForm()
    return render(request, "agendamento.html", {'formAgenda': formAgenda})

def agtSaude(request):
    return render(request, "menuAgtSaude.html")

def agtSecretaria(request):
    return render(request, "menuAgtSecretaria.html")