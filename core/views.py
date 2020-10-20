from django.shortcuts import render, redirect
from .forms import AgendamentoModel, UsuarioModel, DataModel, DeletarData, \
    StatusAgendamento, AlterarDataModel, AlterarAgendamento
from .models import DataPeriodo, Agendamento, Usuario, Atendimento
from django.contrib import messages
from datetime import date
# Create your views here.
def index(request):
    return render(request, 'index.html')

def administracao(request):
    return render(request, 'administracao.html')

def agendamento(request):
    formulario = AgendamentoModel(request.POST or None)
    datas = DataPeriodo.objects.all()

    if formulario.is_valid():
        formulario = Agendamento.objects.create(nome=formulario.cleaned_data['nome'],
                                                cpf=formulario.cleaned_data['cpf'],
                                                rg=formulario.cleaned_data['rg'],
                                                telefone=formulario.cleaned_data['telefone'],
                                                endereco=formulario.cleaned_data['endereco'],
                                                data=formulario.cleaned_data['data'],
                                                codigo_exibicao=formulario.cleaned_data['nome'] + formulario.cleaned_data['cpf'])
        quantidades = DataPeriodo.objects.get(data=formulario.data.data)
        calculo = (quantidades.quantidade) - 1
        data = DataPeriodo.objects.filter(data=formulario.data.data).update(quantidade=calculo)
        messages.success(request, 'O código do seu agendamento é %s' % (formulario.codigo_exibicao))
        formulario.save()

    agendamento = Agendamento.objects.all()
    return render(request, 'agendamento.html', {'datas':datas, 'agendamento':agendamento})

def agendamento_adm(request):
    datas = DataPeriodo.objects.filter(quantidade__gt=0)
    #agendamentos = Agendamento.objects.all()
    formulario = AgendamentoModel(request.POST or None)
    if formulario.is_valid():
        formulario = Agendamento.objects.create(nome=formulario.cleaned_data['nome'],
                                                cpf=formulario.cleaned_data['cpf'],
                                                rg=formulario.cleaned_data['rg'],
                                                telefone=formulario.cleaned_data['telefone'],
                                                endereco=formulario.cleaned_data['endereco'],
                                                data=formulario.cleaned_data['data'],
                                                codigo_exibicao=formulario.cleaned_data['nome'] +
                                                                formulario.cleaned_data['cpf'])
        quantidades = DataPeriodo.objects.get(data=formulario.data.data)
        calculo = (quantidades.quantidade) - 1
        data = DataPeriodo.objects.filter(data=formulario.data.data).update(quantidade=calculo)
        messages.success(request, 'O código do seu agendamento é %s' % (formulario.codigo_exibicao))
        formulario.save()
    return render(request, 'agendamento_adm.html', {'datas':datas})#, 'agendamentos':agendamentos})

def agendamentos_dia(request):
    data_atual = date.today()
    agendamento = Agendamento.objects.filter(data__data='1111-11-11', status='Agendado')
    return render(request, 'agendamentos_dia.html', {'agendamento':agendamento})

def data_adm(request):
    formulario = DataModel(request.POST or None)
    datas = DataPeriodo.objects.filter(quantidade__gt=0)
    if str(request.method == 'POST'):
        if formulario.is_valid():
            formulario.save()
    return render(request, 'data_adm.html', {'datas':datas})

def data_periodos(request):
    formulario = DataModel(request.POST or None)
    datas = DataPeriodo.objects.all()
    if str(request.method == 'POST'):
        if formulario.is_valid():
            formulario.save()
    return render(request, 'data_periodos.html', {'datas':datas})

def funcionarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'funcionarios.html', {'usuarios':usuarios})

def status_agendamento(request):
    #formulario = StatusAgendamento(request.POST or None)
    agendamento = Agendamento.objects.filter(codigo_exibicao=request.POST.get('codigo_exibicao'))

    if not agendamento:
        messages.error(request, 'Agendamento não existe')
        return redirect('agendamento')

    return render(request, 'status_agendamento.html', {'agendamento':agendamento})


def deletar_agendamento(request, pk):
    agendamento = Agendamento.objects.get(codigo_exibicao=pk)
    agendamento.delete()
    return redirect('agendamento')


def visualizar_datas(request):
    datas = DataPeriodo.objects.all()
    return render(request, 'visualizar_datas.html', {'datas':datas})

def excluir_data(request, pk):
    data = DataPeriodo.objects.get(codigo=pk)
    data.delete()
    return redirect('data_periodos')

def administracao_ssp(request):
    usuario = UsuarioModel(request.POST or None)

    if usuario.is_valid():
        print('deu certo')
        usuario.save()
    return render(request, 'administracao_ssp.html')

def confirmar(request, pk):
    agendamento = Agendamento.objects.get(codigo=pk)
    atendimento = Atendimento.objects.create(cod_agendamento=agendamento,
                                             cod_func=request.user)
    atualiza = Agendamento.objects.filter(status='Agendado', codigo=pk).update(status='Confirmado')
    atendimento.save()
    return redirect('agendamentos_dia')

def alterar_data(request, pk):
    data = DataPeriodo.objects.get(codigo=pk)
    formulario = AlterarDataModel(request.POST or None, instance=data)
    if formulario.is_valid():
        formulario.save()
        return redirect('data_adm')
    return render(request, 'alterar_data.html', {'form':formulario})

def alterar_dados(request, pk):
    usuario = Usuario.objects.get(id=pk)

    formulario = UsuarioModel(request.POST or None, instance=usuario)
    if formulario.is_valid():
        formulario.save()
        return redirect('administracao')
    return render(request, 'alterar_dados.html', {'form':formulario})

def perfil(request, username):
    usuario = Usuario.objects.get(username=username)
    return render(request, 'perfil.html', {'usuario':usuario})

def alterar_agendamento(request, pk):
    agendamento = Agendamento.objects.get(codigo_exibicao=pk)

    alterar = AlterarAgendamento(request.POST or None, instance=agendamento)
    datas = DataPeriodo.objects.filter(quantidade__gt=0)
    if alterar.is_valid():
        alterar.save()
        return redirect('agendamento')
    return render(request, 'alterar_agendamento.html', {'agendamento': agendamento, 'form':alterar, 'datas':datas})

def excluir_func(request, pk):
    usuario = Usuario.objects.get(id=pk)
    usuario.delete()
    return redirect('funcionarios')

def projeto(request):
    return render(request, 'projeto.html')