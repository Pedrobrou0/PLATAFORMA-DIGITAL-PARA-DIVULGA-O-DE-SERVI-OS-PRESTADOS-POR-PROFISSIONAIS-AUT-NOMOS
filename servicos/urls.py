from django.urls import path
from . import views


urlpatterns = [
    path(
        'categorias/',
        views.lista_categorias,
        name='lista_categorias'
    ),

    path(
        'categorias/novo/',
        views.criar_categoria,
        name='criar_categoria'
    ),

    path(
        'categorias/<int:id>/',
        views.detalhe_categoria,
        name='detalhe_categoria'
    ),

    path(
        'categorias/<int:id>/editar/',
        views.editar_categoria,
        name='editar_categoria'
    ),

    path(
        'categorias/<int:id>/deletar/',
        views.deletar_categoria,
        name='deletar_categoria'
    ),
]