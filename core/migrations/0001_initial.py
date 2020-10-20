# Generated by Django 3.0.5 on 2020-10-14 21:26

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=8, null=True, verbose_name='RG')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone')),
                ('endereco', models.CharField(blank=True, max_length=50, null=True, verbose_name='Endereço')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('nome', models.CharField(max_length=15, unique=True, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=8, null=True, verbose_name='RG')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone')),
                ('endereco', models.CharField(blank=True, max_length=50, null=True, verbose_name='Endereço')),
                ('codigo_exibicao', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código exibição')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataPeriodo',
            fields=[
                ('codigo', models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='Código')),
                ('data', models.DateField(verbose_name='Data')),
                ('hora_inicio', models.TimeField(verbose_name='Hora de início')),
                ('hora_termino', models.TimeField(verbose_name='Hora de término')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade de vagas')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='Código do atendimento')),
                ('cod_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Agendamento')),
                ('cod_func', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='agendamento',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.DataPeriodo'),
        ),
    ]
