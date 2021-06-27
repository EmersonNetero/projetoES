#from conda.base import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from .models import AgenteSecretaria, AdministradorSistema
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaForm, AgenteSaudeForm, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm
from django.contrib import messages

###

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



# def login(request):
#     if request.method == 'POST':
#         email = request.POST['usuario']
#         senha = request.POST['senha']
#         email_confirm = Profissao.objects.filter(email=email)
#         senha_confirm = Profissao.objects.filter(senha=senha)
#
#         if len(email_confirm) > 0 and len(senha_confirm) > 0:
#             if len(AgenteSaude.objects.filter(email=email)) > 0:
#                 print('agente de saude')  # colocaria a tela do agente de saúde
#                 return redirect('admSistema')
#             elif len(AgenteSecretaria.objects.filter(email=email)) > 0:
#                 print('Agente da secretatia')  # tela do agente de secretaria
#                 return redirect('admSistema')
#             elif len(AdministradorSistema.objects.filter(email=email)) > 0:
#                 print('Administrador do sistema')
#                 return redirect('admSistema')
#
#         else:
#             messages.error(request, "email ou senha errado!!")
#             data = {}
#             data['form'] = LoginForm()
#             return render(request, 'login.html', data)
#
#     else:
#         data = {}
#         data['form'] = LoginForm()
#         return render(request, 'login.html', data)




# Create your views here.
def home(request):
	return render(request, "index.html")

###
# def login(request):
#     data = {}
#     data['form'] = LoginForm()
#     return render(request, 'login.html', data)

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
    f = EnderecoForm()
    head = 3
    if request.method == "POST":
        formEndereco = EnderecoForm(request.POST)
        if formEndereco.is_valid():
            formEndereco.save()
            context['form'] = f
            messages.info(request, "Endereço Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", {'formEn': f, 'head': head})
    else:
        formEndereco = EnderecoForm(prefix='adr')
    context['form'] = formEndereco
    return render(request, "cadDiverso.html", {'formEn': formEndereco, 'head': head})

###
def cadAdmSistema(request):
    if request.method == "POST":
        adm = AdministradorSistemaForm(request.POST)
        formE = EnderecoForm(request.POST)
        if adm.is_valid() and formE.is_valid():
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
