from django.db import models

# Create your models here.

class Endereco(models.Model):
    pk_endereco = models.CharField(max_length=50, primary_key=True)
    logradouro = models.CharField(max_length=20, null=False)
    numero = models.IntegerField(10, null=False)
    bairro = models.CharField(max_length=20, null=False)
    complemento = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=30, null=False)
    uf = models.CharField(max_length=2, null=False)
    cep = models.CharField(max_length=8, null=False)


class Pessoa(models.Model):
    pk_pessoa = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False)
    data_nascimento = models.DateField(null=False)
    telefone = models.IntegerField(12, null=False)
    rg = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=False)
    senha = models.CharField(max_length=25, null=False)
    tipo_usuario = models.CharField(max_length=30, null=False)
    fk_endereco = models.ForeignKey(Endereco, db_column='pk_endereco', on_delete=models.RESTRICT)
