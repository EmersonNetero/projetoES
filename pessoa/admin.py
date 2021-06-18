from django.contrib import admin
from .models import Pessoa, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, DadosProfissional, \
    AdministradorInstituicao, AgenteSaude, Paciente

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(AgenteSecretaria)
admin.site.register(AdministradorSistema)
admin.site.register(Cargo)
admin.site.register(DadosProfissional)
admin.site.register(AdministradorInstituicao)
admin.site.register(AgenteSaude)
admin.site.register(Paciente)