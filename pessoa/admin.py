from django.contrib import admin
from .models import Profissao, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, Pagamento, \
    AgenteSaude, Paciente, Procedimento, TipoProcedimento, Agendamento

admin.site.register(Profissao)
admin.site.register(Endereco)
admin.site.register(AgenteSecretaria)
admin.site.register(AdministradorSistema)
admin.site.register(Cargo)
admin.site.register(Paciente)
admin.site.register(Pagamento)
admin.site.register(AgenteSaude)
admin.site.register(Procedimento)
admin.site.register(TipoProcedimento)
admin.site.register(Agendamento)