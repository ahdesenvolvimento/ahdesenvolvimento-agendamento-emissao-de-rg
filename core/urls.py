from django.urls import path
from .views import index, administracao, agendamento_adm, agendamentos_dia, data_adm, \
    data_periodos, funcionarios, status_agendamento, visualizar_datas, agendamento, \
    excluir_data, deletar_agendamento, administracao_ssp, confirmar, alterar_data, alterar_dados, \
    perfil, alterar_agendamento, excluir_func, projeto

urlpatterns = [
    path('', index, name='index'),
    path('administracao', administracao, name='administracao'),
    path('agendamento_adm', agendamento_adm, name='agendamento_adm'),
    path('agendamentos_dia', agendamentos_dia, name='agendamentos_dia'),
    path('data_adm', data_adm, name='data_adm'),
    path('data_periodos', data_periodos, name='data_periodos'),
    path('funcionarios', funcionarios, name='funcionarios'),
    path('status_agendamento', status_agendamento, name='status_agendamento'),
    path('visualizar_datas', visualizar_datas, name='visualizar_datas'),
    path('agendamento', agendamento, name='agendamento'),
    path('excluir_data/<int:pk>', excluir_data, name='excluir_data'),
    path('deletar_agendamento/<str:pk>', deletar_agendamento, name='deletar_agendamento'),
    path('administracao_ssp', administracao_ssp, name='administracao_ssp'),
    path('confirmar/<int:pk>', confirmar, name='confirmar'),
    path('alterar_data/<int:pk>', alterar_data, name='alterar_data'),
    path('alterar_dados/<int:pk>', alterar_dados, name='alterar_dados'),
    path('perfil/<str:username>', perfil, name='perfil'),
    path('alterar_agendamento/<str:pk>', alterar_agendamento, name='alterar_agendamento'),
    path('excluir_func/<int:pk>', excluir_func, name='excluir_func'),
    path('projeto', projeto, name='projeto'),

]
