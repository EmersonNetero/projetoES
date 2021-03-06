#from conda.base import context
from django.db.models.fields.related import ForeignKey
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Agendamento, AgenteSecretaria, AdministradorSistema, Paciente, Pagamento, AgenteSaude, Profissao, Endereco, Procedimento, TipoProcedimento
from .forms import LoginForm, ProfissaoForm, EnderecoForm, AgenteSecretariaForm, AgenteSaudeForm, AdministradorSistemaForm, CargoForm, \
    TipoProcedimentoForm, AgendamentoForm, PagamentoForm, PacienteForm, ProcedimentoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

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
            use = User.objects.get(username=email)
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
    aux = AdministradorSistema.objects.filter(email=request.user)
    if aux:
        return render(request, "menuAdmSistema.html", {'db': aux[0]})
    return render(request, "menuAdmSistema.html")

def agtSaude(request):
    aux = AgenteSaude.objects.filter(email=request.user)
    aSaude = get_object_or_404(AgenteSaude, email=request.user)
    if aux:
        return render(request, "menuAgtSaude.html", {'db': aux[0], 'ageId': aSaude.pk_agente_saude})
    return render(request, "menuAgtSaude.html")

###
def agtSecretaria(request):
    aux = AgenteSecretaria.objects.filter(email=request.user)
    if aux:
        return render(request, "menuAgtSecretaria.html", {'db': aux[0]})
    return render(request, "menuAgtSecretaria.html")

###
def cadastrarCargo(request):
    context = {}
    user = Profissao.objects.filter(email=request.user)
    f = CargoForm()
    head = 1
    if request.method == "POST":
        formCargo = CargoForm(request.POST)
        if formCargo.is_valid():
            formCargo.save()
            context['form'] = f
            messages.info(request, "Cargo Cadastrado com Sucesso!")
            if user:
                return render(request, "cadDiverso.html", {'formG': f, 'head': head, 'db': user[0]})
            return render(request, "cadDiverso.html", {'formG': f, 'head': head})#, 'db': user[0]})
    else:
        formCargo = CargoForm()
    context['form'] = formCargo
    if user:
        return render(request, "cadDiverso.html", {'formG': f, 'head': head, 'db': user[0]})
    return render(request, "cadDiverso.html", {'formG': formCargo, 'head': head})#, 'db': user[0]})

###
def cadastrarTipoProcedimento(request):
    context = {}
    user = Profissao.objects.filter(email=request.user)
    f = TipoProcedimentoForm
    head = 2
    if request.method == "POST":
        formTipProcedimento = TipoProcedimentoForm(request.POST)
        if formTipProcedimento.is_valid():
            formTipProcedimento.save()
            context['form'] = f
            messages.info(request, "Tipo de Procediemnto Cadastrado com Sucesso!")
            if user:
                return render(request, "cadDiverso.html", {'formTp': f, 'head': head, 'db':user[0]})
            return render(request, "cadDiverso.html", {'formTp': f, 'head': head})
    else:
        formTipProcedimento = TipoProcedimentoForm()
    context['form'] = formTipProcedimento
    if user:
        return render(request, "cadDiverso.html", {'formTp': formTipProcedimento, 'head': head, 'db':user[0]})
    return render(request, "cadDiverso.html", {'formTp': f, 'head': head})


###
def cadastrarPaciente(request):
    context = {}
    user = Profissao.objects.filter(email=request.user)
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
    if user:
        return render(request, "paciente.html", {'formP': formP, 'formE': formE, 'db': user[0]})
    return render(request, "paciente.html", {'formP': formP, 'formE': formE})

###
def cadastraAgntSecretaria(request):
    user = Profissao.objects.filter(email=request.user)
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
    if user:
        return render(request, "agntSecretaria.html", {'formS': formS, 'formE': formE, 'db':user[0]})
    return render(request, "agntSecretaria.html", {'formS': formS, 'formE': formE})

###
def cadastraAgntSaude(request):
    user = Profissao.objects.filter(email=request.user)
    if request.method == "POST":
        saude = AgenteSaudeForm(request.POST, request.FILES)
        formE = EnderecoForm(request.POST)
        if saude.is_valid() and formE.is_valid():
            cria_user_django(request.POST)
            endereco = formE.save()
            agntSaude = saude.save(commit=False)
            agntSaude.fk_endereco = endereco
            agntSaude.save()
            messages.info(request, "Agente de Sa??de cadastrado com sucesso")
            return HttpResponseRedirect("/cadastrarAgntSaude")
    else:
        saude = AgenteSaudeForm()
        formE = EnderecoForm()
    if user:
        return render(request, "agntSaude.html", {'saude': saude, 'formE': formE, 'db':user[0]})
    return render(request, "agntSaude.html", {'saude': saude, 'formE': formE})

###
def cadastrarEndereco(request):
    context = {}
    user = Profissao.objects.filter(email=request.user)
    f = EnderecoForm
    head = 3
    if request.method == "POST":
        formEndereco = EnderecoForm(request.POST)
        if formEndereco.is_valid():
            formEndereco.save()
            context['form'] = f
            messages.info(request, "Endere??o Cadastrado com Sucesso!")
            return render(request, "cadDiverso.html", {'formEn': f, 'head': head, 'db':user[0]})
    else:
        formEndereco = EnderecoForm()
    context['form'] = formEndereco
    return render(request, "cadDiverso.html", {'formEn': formEndereco, 'head': head, 'db':user[0]})

###
def cadAdmSistema(request):
    user = Profissao.objects.filter(email=request.user)
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
    if user:
        return render(request, "cadastroPessoa.html",{'adm': adm, 'formE': formE, 'db':user[0]})
    return render(request, "cadastroPessoa.html",{'adm': adm, 'formE': formE}) #, 'db':user[0]})

###
def agendarConsultas(request):
    url = request.path
    print(url)
    context = {}
    user = Profissao.objects.filter(email=request.user)
    f = AgendamentoForm()
    if request.method == 'POST':
        formAgenda = AgendamentoForm(request.POST)
        if formAgenda.is_valid():
            formAgenda.save()
            context['formAgenda'] = f
            messages.info(request, "Agendamento cadastrado com sucesso!")
            return HttpResponseRedirect(url)
    else:
        formAgenda = AgendamentoForm()
    return render(request, "agendamento.html", {'formAgenda': formAgenda, 'db':user[0], 'url':url})


###
def viewAgendamento(request):
    agendamentos = {}
    user = Profissao.objects.filter(email=request.user)
    agendamentos['db'] = user[0]
    search = request.GET.get('busca')
    if search:
        agendamentos['db2'] = Agendamento.objects.filter(fk_paciente__nome = search).order_by('data_agendamento').reverse()
    else:
        All = Agendamento.objects.all().order_by('data_agendamento').reverse()
        paginator = Paginator(All, 10)
        pages = request.GET.get('page')
        agendamentos['db2'] = paginator.get_page(pages)
    return render(request, 'consultarAgendamento.html', agendamentos)

###
def viewCronograma(request):
    user = Profissao.objects.filter(email=request.user)
    agendamentos = {}
    agendamentos['db'] = user[0]
    All = Agendamento.objects.all()
    paginator = Paginator(All, 10)
    pages = request.GET.get('page')
    agendamentos['db2'] = paginator.get_page(pages)
    return render(request, 'cronograma.html', agendamentos)

def telaPagamento(request):
    agendamentos = {}
    user = Profissao.objects.filter(email=request.user)
    agendamentos['db'] = user[0]
    All = Agendamento.objects.all().order_by('pago')
    paginator = Paginator(All, 10)
    pages = request.GET.get('page')
    agendamentos['db2'] = paginator.get_page(pages)
    return render(request, 'realizarPagamento.html', agendamentos)

def pagar(request, pk):
    pagamentos = {}
    user = Profissao.objects.filter(email=request.user)
    pagamentos['db'] = user[0]
    pago = Agendamento.objects.get(pk_agendamento=pk)
    pago.pago = True
    pago.save()
    pagamentos['db2'] = Agendamento.objects.get(pk_agendamento=pk)
    return render(request, 'pagar.html', pagamentos)

###
def realizarProcedimento(request, age_id):
    context = {}
    user = Profissao.objects.filter(email=request.user)
    f = ProcedimentoForm
    objAgendamento, objPaciente = viewAgendamentoSel(age_id)
    if request.method == "POST":
        formProcedimento = ProcedimentoForm(request.POST)
        if formProcedimento.is_valid():
            formProcedimento.save()
            context['formProcedimento'] = f
            messages.info(request, "Procedimento Realizado com Sucesso!")
            return render(request, "procedimento.html", {'formProcedimento': formProcedimento, 'db':user[0]})
    else:
        formProcedimento = ProcedimentoForm()
    context['formProcedimento'] = formProcedimento
    # context = {
    #     'formProcedimento': formProcedimento,
    #     'ageId': objAgendamento,
    #     'nPaciente': objPaciente,
    #     'aSaude': request.session.get('username'),
    # }
    return render(request, "procedimento.html", {'formProcedimento': formProcedimento, 'db':user[0]})


def viewCronogramaAgtSaude(request, nome):
    agendamentos = {}
    user = Profissao.objects.filter(email=request.user)
    agendamentos['db'] = user[0]
    if nome:
        agendamentos['db2'] = Agendamento.objects.filter(fk_agente_saude__nome = nome)
    else:
        All = Agendamento.objects.all()
        paginator = Paginator(All, 5)
        pages = request.GET.get('page')
        agendamentos['db2'] = paginator.get_page(pages)
    return render(request, 'cronogramAgt.html', agendamentos)


def verAgendamento(request, pk):
    agendamento = {}
    user = Profissao.objects.filter(email=request.user)
    agendamento['db'] = user[0]
    agendamento['db2'] = Agendamento.objects.get(pk_agendamento=pk)
    return render(request, 'viewAgendameto.html', agendamento)


def viewUsuarios(request):
    user = Profissao.objects.filter(email=request.user)
    usuarios = Profissao.objects.all()
    data = {}
    data['db'] = user[0]
    search = request.GET.get('busca')
    if search:
        data['db2'] = Profissao.objects.filter(nome=search)
    else:
        data['db2'] = usuarios
    return render(request, 'usuarios.html', data)


def edit(request, cpf):
    user = Profissao.objects.filter(email=request.user)
    data = {}
    saude = AgenteSaude.objects.filter(cpf=cpf)
    secretaria = AgenteSecretaria.objects.filter(cpf=cpf)
    adm = AdministradorSistema.objects.filter(cpf=cpf)
    data['db'] = user[0]
    if saude:
        data['db2'] = AgenteSaude.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        data['saude'] = AgenteSaudeForm(instance=data['db2'])
        data['formE'] = EnderecoForm(instance=endereco)
        return render(request, 'agntSaude.html', data)

    elif secretaria:
        data['db2'] = AgenteSecretaria.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        data['formE'] = EnderecoForm(instance=endereco)
        data['formS'] = AgenteSecretariaForm(instance=data['db2'])
        return render(request, 'agntSecretaria.html', data)

    elif adm:
        data['db2'] =AdministradorSistema.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        data['formE'] = EnderecoForm(instance=endereco)
        data['adm'] = AdministradorSistemaForm(instance=data['db2'])
        return render(request, 'cadastroPessoa.html', data)


def update(request, cpf):
    user = Profissao.objects.filter(email=request.user)
    data = {}
    saude = AgenteSaude.objects.filter(cpf=cpf)
    secretaria = AgenteSecretaria.objects.filter(cpf=cpf)
    adm = AdministradorSistema.objects.filter(cpf=cpf)
    data['db'] = user[0]
    if saude:
        data['db2'] =AgenteSaude.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        form = AgenteSaudeForm(request.POST or None, instance=data['db2'])
        formE = EnderecoForm(request.POST or None, instance=endereco)
        if form.is_valid() and formE.is_valid():
            form.save()
            formE.save()
            return redirect('admSistema')

    elif secretaria:
        data['db2'] =AgenteSecretaria.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        form = AgenteSecretariaForm(request.POST or None, instance=data['db2'])
        formE = EnderecoForm(request.POST or None, instance=endereco)
        if form.is_valid() and formE.is_valid():
            form.save()
            formE.save()
            return redirect('admSistema')

    elif adm:
        data['db2'] = AdministradorSistema.objects.get(cpf=cpf)
        endereco = Endereco.objects.get(pk_endereco=data['db2'].fk_endereco.pk_endereco)
        form = AdministradorSistemaForm(request.POST or None, instance=data['db2'])
        formE = EnderecoForm(request.POST or None, instance=endereco)
        if form.is_valid() and formE.is_valid():
            form.save()
            formE.save()
            return redirect('admSistema')
###
def viewAgendamentoEsp(request, sau_id):
    agendamentosEsp : {} #Tipo n??o definido, python n??o ?? tipado
    agendamentos = Agendamento.objects.filter(confirmado=True, fk_agente_saude=sau_id) #AQUI SER?? True
    agendamentosEsp = { #Definido din??micamente
        'result': agendamentos,
    }
    return render(request, 'consultarAgendamentoEsp.html', agendamentosEsp)

###
def viewAgendamentoSel(age_id):
    agendamento = get_object_or_404(Agendamento, pk_agendamento=age_id)
    objAgendamento = agendamento.pk_agendamento
    paciente = agendamento.fk_paciente
    objPaciente = paciente.nome
    return objAgendamento, objPaciente

###
def viewProntuarios(request):
    data = {}
    user = Profissao.objects.filter(email=request.user)
    data['db'] = user[0]
    search = request.GET.get('busca')
    if search:
        data['db2'] = Procedimento.objects.filter(fk_paciente__nome=search)
        if data['db2']:
            data['paciente'] = search
    else:
        data['db2'] = Procedimento.objects.all()
    return render(request, 'consultaProntuarios.html', data)