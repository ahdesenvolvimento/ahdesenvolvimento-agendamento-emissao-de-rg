from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not username:
            raise ValueError('Nome de usuário deve ser fornecido')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class Usuario(AbstractUser):
    username = models.CharField('Username', max_length=15, unique=True, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=11, blank=True, null=True)
    rg = models.CharField('RG', max_length=8, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=11, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'rg', 'telefone', 'endereco', 'first_name', 'last_name']
    objects = UserManager()

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class DataPeriodo(models.Model):
    codigo = models.AutoField('Código', primary_key=True)
    data = models.DateField('Data', blank=False, null=False)
    hora_inicio = models.TimeField('Hora de início', blank=False, null=False)
    hora_termino = models.TimeField('Hora de término', blank=False, null=False)
    quantidade = models.IntegerField('Quantidade de vagas', blank=False, null=False)

class Agendamento(Base):
    codigo = models.AutoField('Código', primary_key=True)
    nome = models.CharField('Nome', max_length=15, unique=True, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=11, blank=True, null=True)
    rg = models.CharField('RG', max_length=8, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=11, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=50, blank=True, null=True)
    codigo_exibicao = models.CharField('Código exibição', max_length=10, blank=True, null=True)
    status = models.CharField('Status', default='Agendado', max_length=15)
    data = models.ForeignKey(DataPeriodo, on_delete=models.DO_NOTHING)

class Atendimento(Base):
    codigo = models.AutoField('Código do atendimento', primary_key=True)
    cod_agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    cod_func = models.ForeignKey(Usuario, on_delete=models.CASCADE)