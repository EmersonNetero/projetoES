#from conda.base import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .models import AgenteSecretaria, AdministradorSistema, Cargo, Profissao, AgenteSaude
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaform, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm, AgenteSaudeform
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, "index.html")

###
"""
def login(request):
    data = {}
    data['form'] = LoginForm()
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(username=email, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('admSistema')
        else:
            messages.error(request, "email ou senha errado!!")
            return render(request, 'login.html', data)


    return render(request, 'login.html', data)
"""
def login(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']
        email_confirm = Profissao.objects.filter(email=email)
        senha_confirm = Profissao.objects.filter(senha=senha)

        if len(email_confirm) > 0 and len(senha_confirm) > 0:
            if len(AgenteSaude.objects.filter(email=email)) > 0:
                print('agente de saude')# colocaria a tela do agente de saúde
                return redirect('admSistema')
            elif len(AgenteSecretaria.objects.filter(email=email)) > 0:
                print('Agente da secretatia') # tela do agente de secretaria
                return redirect('admSistema')
            elif len(AdministradorSistema.objects.filter(email=email)) > 0:
                print('Administrador do sistema')
                return redirect('admSistema')

        else:
            messages.error(request, "email ou senha errado!!")
            data = {}
            data['form'] = LoginForm()
            return render(request, 'login.html', data)

    else:
        data = {}
        data['form'] = LoginForm()
        return render(request, 'login.html', data)


# telas do cargos 
def admSistema(request):
    return render(request, "menuAdmSistema.html")

###
def cadastrarCargo(request):
    template = ""
    context = {}
    f = CargoForm()
    if request.method == "POST":
        formCargo = CargoForm(request.POST)
        if formCargo.is_valid():
            formCargo.save()
            context['form'] = f
            messages.info(request, "Cargo Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", context)
    else:
        formCargo = CargoForm()
    context['form'] = formCargo
    return render(request, "cadDiverso.html", context)

###

def cadastrarTipoProcedimento(request):
    context = {}
    f = TipoProcedimentoForm
    if request.method == "POST":
        formTipProcedimento = TipoProcedimentoForm(request.POST)
        if formTipProcedimento.is_valid():
            formTipProcedimento.save()
            context['form'] = f
            messages.info(request, "Tipo de Procediemnto Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", context)
    else:
        formTipProcedimento = TipoProcedimentoForm()
    context['form'] = formTipProcedimento
    return render(request, "cadDiverso.html", context)


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


def cadastraAgntSecretaria(request):
    if request.method == "POST":
        formS = AgenteSecretariaform(request.POST)
        formE = EnderecoForm(request.POST)
        if formS.is_valid() and formE.is_valid():
            endereco = formE.save()
            agntSecretaria = formS.save(commit=False)
            agntSecretaria.fk_endereco = endereco
            agntSecretaria.save()
            messages.info(request, "Agente de secretaria cadastrado com sucesso")
            return HttpResponseRedirect("/cadastrarAgntSecretaria")
    else:
        formS = AgendamentoForm()
        formE = EnderecoForm()
    return render(request, "agntSecretaria.html", {'formS': formS, 'formE': formE})


def cadastraAgntSaude(request):
    if request.method == "POST":
        saude = AgenteSaudeform(request.POST)
        formE = EnderecoForm(request.POST)
        if saude.is_valid() and formE.is_valid():
            endereco = formE.save()
            agntSaude = saude.save(commit=False)
            agntSaude.fk_endereco = endereco
            agntSaude.save()
            messages.info(request, "Agente de Saúde cadastrado com sucesso")
            return HttpResponseRedirect("/cadastrarAgntSaude")
    else:
        saude = AgenteSaudeform()
        formE = EnderecoForm()
    return render(request, "agntSaude.html", {'saude': saude, 'formE': formE})


