from django.db import models

# Create your models here.

class Endereco(models.Model):
    pk_endereco = models.AutoField(primary_key=True, verbose_name = "IdEndereco")
    logradouro = models.CharField(max_length=60, null=False, blank = False)
    numero = models.IntegerField(null=True, verbose_name = "Número")
    bairro = models.CharField(max_length=60, null=False)
    complemento = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank = False)
    uf = models.CharField(max_length=2, null=False, blank = False, verbose_name = "Estado")
    cep = models.CharField(max_length=9, null=False, blank=False)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        db_table = 'endereco'

    def __int__(self):
        return self.pk_endereco


###
class Cargo(models.Model):
    pk_cargo = models.AutoField(primary_key=True, verbose_name = "pkCargo")
    nome = models.CharField(max_length=200, null=False, blank=False, unique=True, verbose_name="Nome do cargo")
    salario = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name="Salário")

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'

    def __int__(self):
         return  self.pk_cargo

###
class Profissao(models.Model):
    pk_profissao = models.AutoField(primary_key=True, verbose_name = "pkProfissao")
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False, unique = True)
    data_nascimento = models.DateField(null=False, blank = False, verbose_name = "data Nascimento")
    telefone = models.CharField(max_length=14, null=False, blank=False)
    rg = models.CharField(max_length=50, null=True, blank=True)
    fotoPerfil = models.FileField(upload_to='static/fotos/', null=True, blank=True, verbose_name="Foto do Perfil")
    matricula = models.CharField(max_length=20, null=False, blank=False, unique=True)
    pis_pasep = models.CharField(max_length=11, blank=True, null=True, unique=True)
    ctps = models.CharField(max_length=20, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=40, null=False, blank=False, verbose_name="Tipo de Usuario")
    email = models.EmailField(max_length=60, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=30, null=False, blank=False)
    fk_endereco = models.ForeignKey('Endereco', db_column='pk_endereco', verbose_name = "fkEndereco", on_delete=models.PROTECT)
    fk_cargo = models.ForeignKey(Cargo, verbose_name="fkCargo", related_name="fk_cargo", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Profissao'
        verbose_name_plural = 'Profissoes'
        db_table = 'profissao'

    def __int__(self):
        return self.pk_profissao

###
class AgenteSecretaria(Profissao):
    pk_agente_secretaria = models.AutoField(primary_key=True, verbose_name = "pk_agente_secretaria")

    class Meta:
        verbose_name = 'AgenteSecretaria'
        verbose_name_plural = 'AgenteSecretarias'
        db_table = 'agente_secretaria'

    def __int__(self):
        return  self.pk_agente_secretaria


###
class AdministradorSistema(Profissao):
    pk_adm_sistema = models.AutoField(primary_key=True, verbose_name = "pk_adm_sistema")

    class Meta:
        verbose_name = 'AdministradorSistema'
        verbose_name_plural = 'AdministradorSistemas'
        db_table = 'administrador_sistema'

    def __int__(self):
        return  self.pk_adm_sistema

###
class AgenteSaude(Profissao):
    pk_agente_saude = models.AutoField(primary_key=True, verbose_name = "pkAgenteSaude")
    tipo_agente_saude = models.CharField(max_length=100, null=False, blank=False)
    conselho_classe = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'AgenteSaude'
        verbose_name_plural = 'Agentes  Saude'
        db_table = 'agente_saude'

    def __int__(self):
        return self.pk_agente_saude

###

class Paciente(models.Model):
    pk_paciente = models.AutoField(primary_key=True, verbose_name="pkPaciente")
    nome = models.CharField(max_length=200, null=False, blank = False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    data_nascimento = models.DateField(null=False, blank=False, verbose_name="data Nascimento")
    telefone = models.CharField(max_length=14, null=False, blank=False)
    rg = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=60, null=True, blank=True, unique=True)
    sangue_tipo = models.CharField(max_length=12, null=True, blank=True)
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    fk_endereco = models.ForeignKey('Endereco', db_column='pk_endereco', verbose_name="fkEndereco",
                                    on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'

    def __int__(self):
        return self.pk_paciente


###
class TipoProcedimento(models.Model):
    pk_tipo_procedimento = models.AutoField(primary_key=True, verbose_name = "pkTipoProcedimento")
    nome = models.CharField(max_length=100, null=False, blank=False, unique=False, verbose_name = "Nome do Procedimento")
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name = "Valor")

    class Meta:
        verbose_name = 'TipoProcedimento'
        verbose_name_plural = 'TiposProcedimento'
        db_table = 'procedimento_tipo'

    def __int__(self):
        return  self.pk_tipo_procediemnto

###
class Agendamento(models.Model):
    TIPOAGENDAMENTO_CHOICE = [
        (1, 'Consulta'),
        (2, 'Exame'),
        (3, 'Cirurgia'),
    ]
    pk_agendamento = models.AutoField(primary_key=True, verbose_name = "pkAgendamento")
    tipo_agendamento = models.IntegerField(choices=TIPOAGENDAMENTO_CHOICE)
    data_agendamento = models.DateField(auto_now_add = True, null=False, blank=False, verbose_name="dataAgendamento")
    pago = models.BooleanField(null = True)
    observacao = models.TextField(max_length=300, null=True, blank=True, unique=False)
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente',
                                             verbose_name="fkPaciente",
                                             on_delete=models.PROTECT)
    fk_tipo_procedimento = models.ForeignKey('TipoProcedimento', db_column='pk_tipo_procedimento',
                                             verbose_name="fkTipoProcedimento",
                                             on_delete=models.PROTECT)
    fk_agente_saude = models.ForeignKey('AgenteSaude', db_column='pk_agente_saude',
                                             verbose_name="fkAgenteSaude", null=True, blank=True,
                                             on_delete=models.PROTECT)
    fk_agente_secretaria = models.ForeignKey('AgenteSecretaria', db_column='pk_agente_secretaria',
                                             verbose_name="fkAgenteSecretaria",
                                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        db_table = 'agendamento'

    def __int__(self):
        return  self.pk_agendamento


###
class Pagamento(models.Model):
    pk_pagamento = models.AutoField(primary_key=True, verbose_name = "pkPagamento")
    data = models.DateField(null=False, blank=False, verbose_name = "Data do Pagamento")
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name = "Valor")
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente',
                                    verbose_name="fkPaciente", on_delete=models.PROTECT)
    fk_agendamento = models.ForeignKey('Agendamento', db_column='pk_agendamento',
                                        verbose_name="fkAgendamento", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        db_table = 'pagamento'

    def __int__(self):
        return  self.pk_pagamento


###
class Procedimento(models.Model):
    pk_procedimento = models.AutoField(primary_key=True, verbose_name = "pkProcedimento")
    medicamento = models.TextField(max_length=300, null=True, blank=True, unique=False)
    comorbidade = models.CharField(max_length=100, null=True, blank=True, unique=False)
    gravidade = models.CharField(max_length=100, null=True, blank=True, unique=False)
    descricao = models.TextField(max_length=300, null=True, blank=True, unique=False)
    observacao = models.TextField(max_length=300, null=True, blank=True, unique=False)
    reaçizado = models.BooleanField(null=True)
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente',
                                             verbose_name="fkPaciente",
                                             on_delete=models.PROTECT)
    fk_agendamento = models.ForeignKey('Agendamento', db_column='pk_agendamento',
                                             verbose_name="fkTipoProcedimento",
                                             on_delete=models.PROTECT)
    fk_agente_saude = models.ForeignKey('AgenteSaude', db_column='pk_agente_saude',
                                             verbose_name="fkAgenteSaude", null=True, blank=True,
                                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'
        db_table = 'procedimento'

    def __int__(self):
        return  self.pk_procedimento