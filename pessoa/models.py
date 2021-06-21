from django.db import models

# Create your models here.

class Pessoa(models.Model):
    USUARIO_CHOICE = [
        (1, 'Administrador da Instituição'),
        (2, 'Administrador do Sistema'),
        (3, 'Agente de Saúde'),
        (4, 'Agente de Secretaria'),
    ]
    pk_pessoa = models.AutoField(primary_key=True, verbose_name = "pkPessoa")
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, unique = True)
    data_nascimento = models.DateField(null=False, blank = False, verbose_name = "dataNascimento")
    telefone = models.CharField(max_length=14, null=False, blank=False)
    rg = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=60, null=False, blank=False, unique = True)
    senha = models.CharField(max_length=30, null=False, blank=False)
    tipo_usuario = models.IntegerField(choices=USUARIO_CHOICE)
    fk_endereco = models.ForeignKey('Endereco', db_column='pk_endereco', verbose_name = "fkEndereco", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

    def __int__(self):
        return self.pk_pessoa

###
class Endereco(models.Model):
    pk_endereco = models.AutoField(primary_key=True, verbose_name = "IdEndereco")
    logradouro = models.CharField(max_length=60, null=False, blank = False)
    numero = models.IntegerField(null=False)
    bairro = models.CharField(max_length=60, null=False)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank = False)
    uf = models.CharField(max_length=2, null=False, blank = False)
    cep = models.CharField(max_length=9, null=False, blank=False)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        db_table = 'endereco'

    def __int__(self):
        return self.pk_endereco

###
class AgenteSecretaria(Pessoa):
    pk_agente_secretaria = models.AutoField(primary_key=True, verbose_name = "pk_agente_secretaria")
    fk_dados_profissional = models.ForeignKey('DadosProfissional', db_column='pk_dados_profissional',
                                              verbose_name="fkDadosProfissional", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'AgenteSecretaria'
        verbose_name_plural = 'AgenteSecretarias'
        db_table = 'agente_secretaria'

    def __int__(self):
        return  self.pk_agente_secretaria###

###
class AdministradorSistema(Pessoa):
    pk_adm_sistema = models.AutoField(primary_key=True, verbose_name = "pk_adm_sistema")
    fk_dados_profissional = models.ForeignKey('DadosProfissional', db_column='pk_dados_profissional',
                                              verbose_name="fkDadosProfissional", on_delete=models.PROTECT)
    fk_dados_profissional = models.ForeignKey('DadosProfissional', db_column='pk_dados_profissional',
                                              verbose_name="fkDadosProfissional", on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'AdministradorSistema'
        verbose_name_plural = 'AdministradorSistemas'
        db_table = 'administrador_sistema'

    def __int__(self):
        return  self.pk_adm_sistema

###
class AgenteSaude(Pessoa):
    pk_agente_saude = models.AutoField(primary_key=True, verbose_name = "pkAgenteSaude")
    tipo_agente_saude = models.CharField(max_length=100, null=False, blank=False)
    conselho_classe = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.CharField(max_length=100, null=True, blank=True)
    fk_dados_profissional = models.ForeignKey('DadosProfissional', db_column='pk_dados_profissional',
                                              verbose_name="fkDadosProfissional", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'AgenteSaude'
        verbose_name_plural = 'Agentes  Saude'
        db_table = 'agente_saude'

    def __int__(self):
        return self.pk_agente_saude


###
class AdministradorInstituicao(AdministradorSistema):
    pk_adm_instituicao = models.AutoField(primary_key=True, verbose_name = "pkAdmInstituicao")

    class Meta:
        verbose_name = 'AdministradorInstituicao'
        verbose_name_plural = 'AdministradoresInstituicao'
        db_table = 'administrador_instituicao'

    def __int__(self):
        return self.pk_adm_instituicao


###
class Paciente(Pessoa):
    pk_paciente = models.AutoField(primary_key=True, verbose_name="pkPaciente")
    sangue_tipo = models.CharField(max_length=12, null=True, blank=True)
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'

    def __int__(self):
        return self.pk_paciente


###
class Cargo(models.Model):
    pk_cargo = models.AutoField(primary_key=True, verbose_name = "pkCargo")
    nome = models.CharField(max_length=200, null=False, blank=False, unique=True)
    salario = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'

    def __int__(self):
        return  self.pk_cargo

###
class DadosProfissional(models.Model):
    pk_dados_profissional = models.AutoField(primary_key=True, verbose_name = "pkDadosProfissionais")
    matricula = models.CharField(max_length=20, null = False, blank = False, unique = True)
    pis_pasep = models.CharField(max_length=11, blank=True, null=True, unique = True)
    ctps = models.CharField(max_length=20, blank=True, null=True)
    fk_cargo = models.ForeignKey('Cargo', db_column='pk_cargo', verbose_name = "fkCargo", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'DadosProfissional'
        verbose_name_plural = 'DadosProfissionais'
        db_table = 'dados_profissional'

    def __int__(self):
        return  self.pk_dados_profissional