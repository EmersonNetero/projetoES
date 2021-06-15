from django.contrib import admin
from .models import Pessoa, Endereco, AgenteSecretaria, AdministradorSistema, Cargo, DadosProfissional

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(AgenteSecretaria)
admin.site.register(AdministradorSistema)
admin.site.register(Cargo)
admin.site.register(DadosProfissional)