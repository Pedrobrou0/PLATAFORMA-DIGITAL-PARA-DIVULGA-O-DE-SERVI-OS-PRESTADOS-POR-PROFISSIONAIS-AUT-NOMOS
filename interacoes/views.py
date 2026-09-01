from django.shortcuts import render, redirect
from .models import Solicitacao
from .forms import SolicitacaoForm, SolicitacaoEditarForm


def lista_solicitacoes(request):
    solicitacoes = Solicitacao.objects.all()

    return render(request, 'interacoes/lista.html', {
        'solicitacoes': solicitacoes
    })


def detalhe_solicitacao(request, id):
    solicitacao = Solicitacao.objects.get(id=id)

    return render(request, 'interacoes/detalhe.html', {
        'solicitacao': solicitacao
    })


def criar_solicitacao(request):
    form = SolicitacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        solicitacoes = Solicitacao.objects.all()

        return render(request, 'interacoes/lista.html', {
            'solicitacoes': solicitacoes
        })

    return render(request, 'interacoes/form.html', {
        'form': form
    })


def editar_solicitacao(request, id):
    solicitacao = Solicitacao.objects.get(id=id)

    form = SolicitacaoEditarForm(
        request.POST or None,
        instance=solicitacao
    )

    if form.is_valid():
        form.save()
        solicitacoes = Solicitacao.objects.all()

        return render(request, 'interacoes/lista.html', {
            'solicitacoes': solicitacoes
        })

    return render(request, 'interacoes/form.html', {
        'form': form
    })


def deletar_solicitacao(request, id):
    solicitacao = Solicitacao.objects.get(id=id)

    if request.method == 'POST':
        solicitacao.delete()

        return redirect('lista_solicitacoes')

    return render(request, 'interacoes/confirmar_delete.html', {
        'objeto': solicitacao,
        'lista_url': 'lista_solicitacoes'
    })