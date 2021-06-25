#from conda.base import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import AgenteSecretaria, AdministradorSistema
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaform, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm
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
