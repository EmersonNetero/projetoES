
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login, cadastrarPessoa, cadastrarEndereco, cadastrarAgenteSecretaria,\
    cadastrarAdministradorSistema, listaAgenteSecretaria, listaAdministradorSistema,\
    detalheAgenteSecretaria, detalheAdministradorSistema, cadastrarCargo, cadastrarDadosProfissional, \
    admSistema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login) ,
    path('', login),
    path('admsistema/', admSistema),
    path('cadastroPeople', cadastrarPessoa)
]
