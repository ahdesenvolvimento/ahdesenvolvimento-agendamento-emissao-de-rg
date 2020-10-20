from django import forms
from .models import Agendamento, DataPeriodo, Usuario

class AgendamentoModel(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'cpf', 'rg', 'telefone', 'endereco', 'data']
        exclude = ['codigo', 'codigo_exibicao']

class DataModel(forms.ModelForm):
    class Meta:
        model = DataPeriodo
        fields = ['data', 'hora_inicio', 'hora_termino', 'quantidade']

class DeletarData(forms.ModelForm):
    class Meta:
        model = DataPeriodo
        fields = ['data']

class StatusAgendamento(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['codigo_exibicao']

class UsuarioModel(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'rg', 'telefone', 'endereco', 'first_name', 'last_name', 'password']

    def save(self, commit=True):
        user = super(UsuarioModel, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class AlterarDataModel(forms.ModelForm):
    class Meta:
        model = DataPeriodo
        fields = ['hora_inicio', 'hora_termino', 'quantidade']

class AlterarDadosModel(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'rg', 'telefone', 'endereco', 'first_name', 'last_name', 'password']

class AlterarAgendamento(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data']