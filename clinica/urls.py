
from django.contrib import admin
from django.urls import path
from pessoa.views import home, login, \
    cadastrarCargo, admSistema, cadastrarTipoProcedimento, cadastrarPaciente


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', login),
    path('', login),
    path('admsistema/', admSistema),
    path('cadastroCargo/', cadastrarCargo),
    path('cadastroTProced/', cadastrarTipoProcedimento),
    path('cadastrarPaciente/', cadastrarPaciente),

]
