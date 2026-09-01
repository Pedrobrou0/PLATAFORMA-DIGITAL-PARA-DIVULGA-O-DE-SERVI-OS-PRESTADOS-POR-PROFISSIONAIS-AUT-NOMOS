from django.shortcuts import render, redirect
from .models import Categoria, Servico
from .forms import CategoriaForm, ServicoForm


def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'servicos/categoria_lista.html', {
        'categorias': categorias
    })


def detalhe_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    return render(request, 'servicos/categoria_detalhe.html', {
        'categoria': categoria
    })


def criar_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        categorias = Categoria.objects.all()

        return render(request, 'servicos/categoria_lista.html', {
            'categorias': categorias
        })

    return render(request, 'servicos/categoria_form.html', {
        'form': form
    })


def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    form = CategoriaForm(
        request.POST or None,
        instance=categoria
    )

    if form.is_valid():
        form.save()
        categorias = Categoria.objects.all()

        return render(request, 'servicos/categoria_lista.html', {
            'categorias': categorias
        })

    return render(request, 'servicos/categoria_form.html', {
        'form': form
    })


def deletar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()

        return redirect('lista_categorias')

    return render(request, 'servicos/confirmar_delete.html', {
        'objeto': categoria,
        'lista_url': 'lista_categorias'
    })