
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login_user, \
    cadastrarCargo, admSistema, cadastrarTipoProcedimento, cadastrarPaciente, cadastraAgntSecretaria, cadastraAgntSaude, \
    cadastrarEndereco, cadAdmSistema, agendarConsultas


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', login),
    path('', login_user, name='login'),
    path('admsistema/', admSistema, name='admSistema'),
    path('cadastroCargo/', cadastrarCargo),
    path('cadastroTProced/', cadastrarTipoProcedimento),
    path('cadastrarPaciente/', cadastrarPaciente),
    path('cadastrarEndereco/', cadastrarEndereco),
    path('cadastrarAgntSecretaria/', cadastraAgntSecretaria, name='cadastrarAgntSecretaria'),
    path('cadastrarAgntSaude/', cadastraAgntSaude, name='cadastrarAgntSaude'),
    path('cadAdmSistema/', cadAdmSistema),
    path('agendamento/', agendarConsultas, name='agendamento')


]
