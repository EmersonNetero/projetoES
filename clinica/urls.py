
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login, \
    cadastrarCargo, admSistema, cadastrarTipoProcedimento, cadastrarPaciente, cadastraAgntSecretaria, cadastraAgntSaude


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', login),
    path('', login),
    path('admsistema/', admSistema, name='admSistema'),
    #path('cadastroAdministrador/', cadastrarAdministradorSistema),
    #path('cadastroEndereco/', cadastrarEndereco),
    path('cadastroCargo/', cadastrarCargo, name='cadastroCargo'),
    path('cadastroTProced/', cadastrarTipoProcedimento, name='cadastroTProced'),
    #path('agendamentoTeste/', cadastrarAgendmentoTeste),
    #path('pagamentoTeste/', cadastrarPagamentoTeste),
    path('cadastrarPaciente/', cadastrarPaciente, name='cadastrarPaciente'),
    path('cadastrarAgntSecretaria/', cadastraAgntSecretaria, name='cadastrarAgntSecretaria'),
    path('cadastrarAgntSaude/', cadastraAgntSaude, name='cadastrarAgntSaude')

]
