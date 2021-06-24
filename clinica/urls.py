
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login, \
    cadastrarEndereco, cadastrarAdministradorSistema, cadastrarCargo, admSistema, cadastrarTipoProcedimento, \
    cadastrarAgendmentoTeste, cadastrarPagamentoTeste


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', login),
    path('', login),
    path('admsistema/', admSistema),
    path('cadastroAdministrador/', cadastrarAdministradorSistema),
    path('cadastroEndereco/', cadastrarEndereco),
    path('cadastroCargo/', cadastrarCargo),
    path('cadastroTProced/', cadastrarTipoProcedimento),
    path('agendamentoTeste/', cadastrarAgendmentoTeste),
    path('pagamentoTeste/', cadastrarPagamentoTeste),


]
