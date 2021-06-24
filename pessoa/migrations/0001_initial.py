# Generated by Django 3.2.4 on 2021-06-24 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('pk_agendamento', models.AutoField(primary_key=True, serialize=False, verbose_name='pkAgendamento')),
                ('tipo_agendamento', models.IntegerField(choices=[(1, 'Consulta'), (2, 'Exame'), (3, 'Cirurgia')])),
                ('data_agendamento', models.DateField(auto_now_add=True, verbose_name='dataAgendamento')),
                ('realizado', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'db_table': 'agendamento',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('pk_cargo', models.AutoField(primary_key=True, serialize=False, verbose_name='pkCargo')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do cargo')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Salário')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'cargo',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('pk_endereco', models.AutoField(primary_key=True, serialize=False, verbose_name='IdEndereco')),
                ('logradouro', models.CharField(max_length=60)),
                ('numero', models.IntegerField(null=True, verbose_name='Número')),
                ('bairro', models.CharField(max_length=60)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('cidade', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9)),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
                'db_table': 'endereco',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pk_paciente', models.AutoField(primary_key=True, serialize=False, verbose_name='pkPaciente')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField(verbose_name='dataNascimento')),
                ('telefone', models.CharField(max_length=14)),
                ('rg', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=60, null=True, unique=True)),
                ('sangue_tipo', models.CharField(blank=True, max_length=12, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('altura', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('fk_endereco', models.ForeignKey(db_column='pk_endereco', on_delete=django.db.models.deletion.PROTECT, to='pessoa.endereco', verbose_name='fkEndereco')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('pk_profissao', models.AutoField(primary_key=True, serialize=False, verbose_name='pkProfissao')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField(verbose_name='dataNascimento')),
                ('telefone', models.CharField(max_length=14)),
                ('rg', models.CharField(blank=True, max_length=50, null=True)),
                ('fotoPerfil', models.CharField(blank=True, max_length=60, null=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to='', verbose_name='Upload da Foto')),
                ('matricula', models.CharField(max_length=20, unique=True)),
                ('pis_pasep', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('ctps', models.CharField(blank=True, max_length=20, null=True)),
                ('tipo_usuario', models.IntegerField(choices=[(1, 'Administrador do Sistema'), (2, 'Agente de Saúde'), (3, 'Agente de Secretaria')])),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('senha', models.CharField(max_length=30)),
                ('fk_cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_cargo', to='pessoa.cargo', verbose_name='fkCargo')),
                ('fk_endereco', models.ForeignKey(db_column='pk_endereco', on_delete=django.db.models.deletion.PROTECT, to='pessoa.endereco', verbose_name='fkEndereco')),
            ],
            options={
                'verbose_name': 'Profissao',
                'verbose_name_plural': 'Profissoes',
                'db_table': 'profissao',
            },
        ),
        migrations.CreateModel(
            name='TipoProcedimento',
            fields=[
                ('pk_tipo_procedimento', models.AutoField(primary_key=True, serialize=False, verbose_name='pkTipoProcedimento')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Procedimento')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'TipoProcedimento',
                'verbose_name_plural': 'TiposProcedimento',
                'db_table': 'procedimento_tipo',
            },
        ),
        migrations.CreateModel(
            name='AdministradorSistema',
            fields=[
                ('profissao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.profissao')),
                ('pk_adm_sistema', models.AutoField(primary_key=True, serialize=False, verbose_name='pk_adm_sistema')),
            ],
            options={
                'verbose_name': 'AdministradorSistema',
                'verbose_name_plural': 'AdministradorSistemas',
                'db_table': 'administrador_sistema',
            },
            bases=('pessoa.profissao',),
        ),
        migrations.CreateModel(
            name='AgenteSaude',
            fields=[
                ('profissao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.profissao')),
                ('pk_agente_saude', models.AutoField(primary_key=True, serialize=False, verbose_name='pkAgenteSaude')),
                ('tipo_agente_saude', models.CharField(max_length=100)),
                ('conselho_classe', models.CharField(max_length=100)),
                ('especialidade', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'AgenteSaude',
                'verbose_name_plural': 'Agentes  Saude',
                'db_table': 'agente_saude',
            },
            bases=('pessoa.profissao',),
        ),
        migrations.CreateModel(
            name='AgenteSecretaria',
            fields=[
                ('profissao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoa.profissao')),
                ('pk_agente_secretaria', models.AutoField(primary_key=True, serialize=False, verbose_name='pk_agente_secretaria')),
            ],
            options={
                'verbose_name': 'AgenteSecretaria',
                'verbose_name_plural': 'AgenteSecretarias',
                'db_table': 'agente_secretaria',
            },
            bases=('pessoa.profissao',),
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('pk_pagamento', models.AutoField(primary_key=True, serialize=False, verbose_name='pkPagamento')),
                ('data', models.DateField(verbose_name='Data do Pagamento')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Valor')),
                ('fk_agendamento', models.ForeignKey(db_column='pk_agendamento', on_delete=django.db.models.deletion.PROTECT, to='pessoa.agendamento', verbose_name='fkAgendamento')),
                ('fk_paciente', models.ForeignKey(db_column='pk_paciente', on_delete=django.db.models.deletion.PROTECT, to='pessoa.paciente', verbose_name='fkPaciente')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'pagamento',
            },
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fk_paciente',
            field=models.ForeignKey(db_column='pk_paciente', on_delete=django.db.models.deletion.PROTECT, to='pessoa.paciente', verbose_name='fkPaciente'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fk_tipo_procedimento',
            field=models.ForeignKey(db_column='pk_tipo_procedimento', on_delete=django.db.models.deletion.PROTECT, to='pessoa.tipoprocedimento', verbose_name='fkTipoProcedimento'),
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('pk_procedimento', models.AutoField(primary_key=True, serialize=False, verbose_name='pkProcedimento')),
                ('medicamento', models.TextField(blank=True, max_length=300, null=True)),
                ('comorbidade', models.CharField(blank=True, max_length=100, null=True)),
                ('gravidade', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField(blank=True, max_length=300, null=True)),
                ('fk_agendamento', models.ForeignKey(db_column='pk_agendamento', on_delete=django.db.models.deletion.PROTECT, to='pessoa.agendamento', verbose_name='fkTipoProcedimento')),
                ('fk_paciente', models.ForeignKey(db_column='pk_paciente', on_delete=django.db.models.deletion.PROTECT, to='pessoa.paciente', verbose_name='fkPaciente')),
                ('fk_agente_saude', models.ForeignKey(blank=True, db_column='pk_agente_saude', null=True, on_delete=django.db.models.deletion.PROTECT, to='pessoa.agentesaude', verbose_name='fkAgenteSaude')),
            ],
            options={
                'verbose_name': 'Procedimento',
                'verbose_name_plural': 'Procedimentos',
                'db_table': 'procedimento',
            },
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fk_agente_saude',
            field=models.ForeignKey(blank=True, db_column='pk_agente_saude', null=True, on_delete=django.db.models.deletion.PROTECT, to='pessoa.agentesaude', verbose_name='fkAgenteSaude'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='fk_agente_secretaria',
            field=models.ForeignKey(db_column='pk_agente_secretaria', on_delete=django.db.models.deletion.PROTECT, to='pessoa.agentesecretaria', verbose_name='fkAgenteSecretaria'),
        ),
    ]