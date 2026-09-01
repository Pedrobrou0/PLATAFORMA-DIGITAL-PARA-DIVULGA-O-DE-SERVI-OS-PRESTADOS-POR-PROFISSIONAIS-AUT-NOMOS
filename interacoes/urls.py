from django.urls import path
from . import views


urlpatterns = [
    path(
        'solicitacoes/',
        views.lista_solicitacoes,
        name='lista_solicitacoes'
    ),

    path(
        'solicitacoes/novo/',
        views.criar_solicitacao,
        name='criar_solicitacao'
    ),

    path(
        'solicitacoes/<int:id>/',
        views.detalhe_solicitacao,
        name='detalhe_solicitacao'
    ),

    path(
        'solicitacoes/<int:id>/editar/',
        views.editar_solicitacao,
        name='editar_solicitacao'
    ),

    path(
        'solicitacoes/<int:id>/deletar/',
        views.deletar_solicitacao,
        name='deletar_solicitacao'
    ),
]