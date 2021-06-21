
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login, adm,cadastrarPessoa, cadastrarEndereco, cadastrarAgenteSecretaria,\
    cadastrarAdministradorSistema, listaAgenteSecretaria, listaAdministradorSistema,\
    detalheAgenteSecretaria, detalheAdministradorSistema, cadastrarCargo, cadastrarDadosProfissional


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login) ,
    path('', home),
    path('admsistema/', adm),
    path('cadastroPeople', cadastrarPessoa)
]
