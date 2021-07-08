from django.db import models

# Create your models here.

class Endereco(models.Model):
    pk_endereco = models.AutoField(primary_key=True, verbose_name = "IdEndereco")
    logradouro  = models.CharField(max_length=60, null=False, blank = False, verbose_name="Logradouro *")
    numero = models.IntegerField(null=True, verbose_name = "Número")
    bairro = models.CharField(max_length=60, null=False, blank=False, verbose_name="Bairro *")
    complemento = models.CharField(max_length=60, null=True, blank=True)
    cidade = models.CharField(max_length=60, null=False, blank = False, verbose_name="Cidade *")
    uf = models.CharField(max_length=2, null=False, blank = False, verbose_name = "Estado *")
    cep = models.CharField(max_length=9, null=False, blank=False, verbose_name="CEP *")

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
        db_table = 'endereco'

    def __str__(self):
        return self.logradouro


###
class Cargo(models.Model):
    pk_cargo = models.AutoField(primary_key=True, verbose_name = "pkCargo")
    nome = models.CharField(max_length=200, null=False, blank=False, unique=True, verbose_name="Nome do cargo *")
    salario = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name="Salário *")

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        db_table = 'cargo'

    def __str__(self):
         return  self.nome

###
class Profissao(models.Model):
    pk_profissao = models.AutoField(primary_key=True, verbose_name = "pkProfissao")
    nome = models.CharField(max_length=200, null=False, blank=False, verbose_name="Nome *")
    cpf = models.CharField(max_length=11, null=False, unique = True, blank=False, verbose_name="CPF *")
    data_nascimento = models.DateField(null=False, blank = False, verbose_name = "Data Nascimento *")
    telefone = models.CharField(max_length=14, null=False, blank=False, verbose_name="Telefone *")
    rg = models.CharField(max_length=50, null=True, blank=True, verbose_name="RG")
    fotoPerfil = models.FileField(upload_to='fotos/', null=True, blank=True, verbose_name="Foto do Perfil")
    matricula = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name="Matrícula *")
    pis_pasep = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name="PIS PASEP")
    ctps = models.CharField(max_length=20, blank=True, null=True, verbose_name="Carteira Trabalho")
    email = models.EmailField(max_length=60, null=False, blank=False, unique=True, verbose_name="E-mail *")
    senha = models.CharField(max_length=30, null=False, blank=False, verbose_name="Senha *")
    fk_endereco = models.ForeignKey('Endereco', db_column='pk_endereco', verbose_name = "fkEndereco", on_delete=models.PROTECT)
    fk_cargo = models.ForeignKey(Cargo, verbose_name="Cargo *", related_name="fk_cargo", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Profissao'
        verbose_name_plural = 'Profissoes'
        db_table = 'profissao'

    def __str__(self):
        return self.nome

###
class AgenteSecretaria(Profissao):
    pk_agente_secretaria = models.AutoField(primary_key=True, verbose_name = "pk_agente_secretaria")
    tipo_usuario = models.CharField(max_length=40, null=False, blank=False, default="Agente de Secretaria", verbose_name="Tipo de Usuario *")

    class Meta:
        verbose_name = 'AgenteSecretaria'
        verbose_name_plural = 'AgenteSecretarias'
        db_table = 'agente_secretaria'

    def __str__(self):
        return  self.nome


###
class AdministradorSistema(Profissao):
    pk_adm_sistema = models.AutoField(primary_key=True, verbose_name = "pk_adm_sistema")
    tipo_usuario = models.CharField(max_length=40, null=False, blank=False, default="Adm do Sistema", verbose_name="Tipo de Usuario *")

    class Meta:
        verbose_name = 'AdministradorSistema'
        verbose_name_plural = 'AdministradorSistemas'
        db_table = 'administrador_sistema'

    def __str__(self):
        return  self.nome

###
class AgenteSaude(Profissao):
    pk_agente_saude = models.AutoField(primary_key=True, verbose_name = "pkAgenteSaude")
    tipo_agente_saude = models.CharField(max_length=100, null=False, blank=False, verbose_name="Tipo Agente de Saúde *")
    conselho_classe = models.CharField(max_length=100, null=False, blank=False, verbose_name="Conselho Classe *")
    especialidade = models.CharField(max_length=100, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=40, null=False, blank=False, default="Agente de Saúde",  verbose_name="Tipo de Usuario *")

    class Meta:
        verbose_name = 'AgenteSaude'
        verbose_name_plural = 'Agentes  Saude'
        db_table = 'agente_saude'

    def __str__(self):
        return self.nome

###

class Paciente(models.Model):
    pk_paciente = models.AutoField(primary_key=True, verbose_name="pkPaciente")
    nome = models.CharField(max_length=200, null=False, blank = False, verbose_name="Nome *")
    cpf = models.CharField(max_length=11, null=False, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(null=False, blank=False, verbose_name="Data Nascimento *")
    telefone = models.CharField(max_length=14, null=False, blank=False, verbose_name="Telefone *")
    rg = models.CharField(max_length=50, null=True, blank=True, verbose_name="Carteira Identidade")
    email = models.EmailField(max_length=60, null=True, blank=True, unique=True, verbose_name="E-mail")
    sangue_tipo = models.CharField(max_length=12, null=True, blank=True, verbose_name="Tipo de Sangue")
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    fk_endereco = models.ForeignKey('Endereco', db_column='pk_endereco', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'paciente'

    def __str__(self):
        return self.nome


###
class TipoProcedimento(models.Model):
    pk_tipo_procedimento = models.AutoField(primary_key=True, verbose_name = "pkTipoProcedimento")
    nome = models.CharField(max_length=100, null=False, blank=False, unique=False, verbose_name = "Nome do Procedimento *")
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name = "Valor *")

    class Meta:
        verbose_name = 'TipoProcedimento'
        verbose_name_plural = 'TiposProcedimento'
        db_table = 'procedimento_tipo'

    def __str__(self):
        return  self.nome

###
class Agendamento(models.Model):
    pk_agendamento = models.AutoField(primary_key=True, verbose_name = "pkAgendamento")
    tipo_agendamento = models.CharField(max_length=30, null=False, blank=False, verbose_name="Tipo de Agendamento *")
    data_agendamento = models.DateField(auto_now_add = True, null=False, blank=False, verbose_name="Data do Agendamento *")
    pago = models.BooleanField(null = True, default=False)
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name="Valor *")
    observacao = models.TextField(max_length=300, null=True, blank=True, unique=False, verbose_name="Observação")
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente', blank=False,
                                             verbose_name="Paciente *",
                                             on_delete=models.PROTECT)
    fk_tipo_procedimento = models.ForeignKey('TipoProcedimento', db_column='pk_tipo_procedimento', blank=False,
                                             verbose_name="Tipo de Procedimento *",
                                             on_delete=models.PROTECT)
    fk_agente_saude = models.ForeignKey('AgenteSaude', db_column='pk_agente_saude',
                                             verbose_name="Agente de Saúde", null=True, blank=True,
                                             on_delete=models.PROTECT)
    fk_agente_secretaria = models.ForeignKey('AgenteSecretaria', db_column='pk_agente_secretaria',
                                             verbose_name="Agente de Secretaria *", blank=False,
                                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        db_table = 'agendamento'

    def __str__(self):
        return  self.fk_paciente


###
class Pagamento(models.Model):
    pk_pagamento = models.AutoField(primary_key=True, verbose_name = "pkPagamento")
    data = models.DateField(null=False, blank=False, verbose_name = "Data do Pagamento *")
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=False, null=False, verbose_name = "Valor *")
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente',
                                    verbose_name="Paciente *", on_delete=models.PROTECT)
    fk_agendamento = models.ForeignKey('Agendamento', db_column='pk_agendamento',
                                        verbose_name="Agendamento *", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        db_table = 'pagamento'

    def __str__(self):
        return  self.fk_paciente


###
class Procedimento(models.Model):
    pk_procedimento = models.AutoField(primary_key=True, verbose_name = "pkProcedimento")
    medicamento = models.TextField(max_length=300, null=True, blank=True, unique=False)
    comorbidade = models.CharField(max_length=100, null=True, blank=True, unique=False)
    gravidade = models.CharField(max_length=100, null=True, blank=True, unique=False)
    descricao = models.TextField(max_length=300, null=True, blank=True, unique=False, verbose_name="Descrição")
    observacao = models.TextField(max_length=300, null=True, blank=True, unique=False, verbose_name="Observação")
    realizado = models.BooleanField(null=True, default=False)
    fk_paciente = models.ForeignKey('Paciente', db_column='pk_paciente', blank=False,
                                             verbose_name="Paciente *",
                                             on_delete=models.PROTECT)
    fk_agendamento = models.ForeignKey('Agendamento', db_column='pk_agendamento', blank=False,
                                             verbose_name="Tipo de Procedimento *",
                                             on_delete=models.PROTECT)
    fk_agente_saude = models.ForeignKey('AgenteSaude', db_column='pk_agente_saude',
                                             verbose_name="Agente de Saúde *", null=True, blank=True,
                                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Procedimento'
        verbose_name_plural = 'Procedimentos'
        db_table = 'procedimento'

    def __str__(self):
        return  self.fk_paciente