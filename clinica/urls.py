from django.contrib import admin
from django.urls import path
from pessoa.views import home, login_user, \
    cadastrarCargo, admSistema, cadastrarTipoProcedimento, cadastrarPaciente, cadastraAgntSecretaria, cadastraAgntSaude, \
    cadastrarEndereco, cadAdmSistema, agendarConsultas, agtSaude, agtSecretaria, logout_user, pagar, telaPagamento, verAgendamento, \
    viewAgendamento, realizarProcedimento, viewCronograma, viewCronogramaAgtSaude, viewUsuarios, edit, update,\
    addProcedimento, viewAgendamentoEsp, viewProntuarios #agendarCirurgias agendarExames




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_user, name='login'),
    path('logout/', logout_user),
    path('admsistema/', admSistema, name='admSistema'),
    path('cadastroCargo/', cadastrarCargo),
    path('cadastroTProced/', cadastrarTipoProcedimento),
    path('cadastrarPaciente/', cadastrarPaciente),
    path('cadastrarEndereco/', cadastrarEndereco),
    path('cadastrarAgntSecretaria/', cadastraAgntSecretaria, name='cadastrarAgntSecretaria'),
    path('cadastrarAgntSaude/', cadastraAgntSaude, name='cadastrarAgntSaude'),
    path('cadAdmSistema/', cadAdmSistema),
    path('agendarConsultas/', agendarConsultas, name='agendamento'),
    path('agendarExames/', agendarConsultas), #AgendarConsultas, pode mudar para agendamentos
    path('agendarCirurgias/', agendarConsultas),
    path('agtSaude/', agtSaude, name='agtSaude'),
    path('agtSecretaria/', agtSecretaria, name='agtSecretaria'),
    path('consultarAgendamento/', viewAgendamento),
    path('realProcedimento/', realizarProcedimento),
    path('cronograma/', viewCronograma),
    path('telapagamento/', telaPagamento),
    path('pagar/<int:pk>/', pagar), 
    path('cronogramaAgtSaude/<slug:nome>', viewCronogramaAgtSaude),
    path('verAgendamento/<int:pk>/', verAgendamento),
    path('usuarios/', viewUsuarios),
    path('edit/<slug:cpf>/', edit),
    path('update/<slug:cpf>/', update),
    path('addProcedimento/<int:age_id>', addProcedimento),
    path('consultarAgendamentoEsp/', viewAgendamentoEsp),
    path('consultaProntuarios/', viewProntuarios),
]