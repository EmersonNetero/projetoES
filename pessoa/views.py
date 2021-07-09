#from conda.base import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Agendamento, AgenteSecretaria, AdministradorSistema, Pagamento, AgenteSaude
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaForm, AgenteSaudeForm, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm, ProcedimentoForm
from django.contrib import messages
from django.core.paginator import Paginator


###
def cria_user_django(info):
    user = User.objects.create_user(info['email'], info['email'], info['senha'])
    user.first_name = info['nome']
    user.last_name = ' '
    user.save()

###

def redirect_to_menu(user):
    saude = AgenteSaude.objects.filter(email=user)
    secretaria = AgenteSecretaria.objects.filter(email=user)
    adm = AdministradorSistema.objects.filter(email=user)
    if saude:
        return redirect('agtSaude')
    elif secretaria:
        return redirect('agtSecretaria')
    elif adm:
        return redirect('admSistema')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['usuario']
        senha = request.POST['senha']
        usuario = authenticate(request, username=email, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect_to_menu(request.POST['usuario'])     
        else:
            messages.error(request, "email ou senha errado!!")
            return render(request, 'login.html')
    return render(request, 'login.html')

###
def logout_user(request):
    logout(request)
    return redirect('login')


###
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
        formS = AgenteSecretariaForm(request.POST, request.FILES)
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
        saude = AgenteSaudeForm(request.POST, request.FILES)
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
        adm = AdministradorSistemaForm(request.POST, request.FILES)
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

###
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

###
def agtSaude(request):
    return render(request, "menuAgtSaude.html")

###
def agtSecretaria(request):
    return render(request, "menuAgtSecretaria.html")

###
def viewAgendamento(request):
    agendamentos = {}
    All = Agendamento.objects.all()
    paginator = Paginator(All, 5)
    pages = request.GET.get('page')
    agendamentos['db'] = paginator.get_page(pages)
    return render(request, 'consultarAgendamento.html', agendamentos)

def viewCronograma(request):
    agendamentos = {}
    All = Agendamento.objects.all()
    paginator = Paginator(All, 5)
    pages = request.GET.get('page')
    agendamentos['db'] = paginator.get_page(pages)
    return render(request, 'cronograma.html', agendamentos)

def telaPagamento(request):
    agendamentos = {}
    All = Agendamento.objects.all()
    paginator = Paginator(All, 5)
    pages = request.GET.get('page')
    agendamentos['db'] = paginator.get_page(pages)
    return render(request, 'realizarPagamento.html', agendamentos)

def pagar(request, pk):
    pagamentos = {}
    formPagamento = PagamentoForm(request.POST or None)
    pagamentos['db'] = Agendamento.objects.get(pk=pk)
    formPagamento.data = pagamentos['db'].data_agendamento
    formPagamento.valor = pagamentos['db'].valor
    formPagamento.fk_paciente = pagamentos['db'].fk_paciente
    formPagamento.fk_agendamento = pagamentos['db'].pk_agendamento
    formPagamento.save()
    formAgendamento = AgendamentoForm(request.POST or None, instace=pagamentos['db'])
    formAgendamento.pago = True
    formAgendamento.save()
    return render(request, 'pagar.html', pagamentos)
###
def realizarProcedimento(request):
    context = {}
    f = ProcedimentoForm
    if request.method == "POST":
        formProcedimento = ProcedimentoForm(request.POST)
        if formProcedimento.is_valid():
            formProcedimento.save()
            context['formProcedimento'] = f
            messages.info(request, "Procedimento Realizado com Sucesso!")
            return render(request, "procedimento.html", {'formProcedimento': formProcedimento})
    else:
        formProcedimento = ProcedimentoForm()
    context['formProcedimento'] = formProcedimento
    return render(request, "procedimento.html", {'formProcedimento': formProcedimento})

def viewCronogramaAgtSaude(request):
    agendamentos = {}
    All = Agendamento.objects.all()
    Allagt = AgenteSaude.objects.all()
    paginator = Paginator(All, 5)
    pages = request.GET.get('page')
    agendamentos['db'] = paginator.get_page(pages)
    agendamentos['agts'] = Allagt
    return render(request, 'cronogramAgt.html', agendamentos)