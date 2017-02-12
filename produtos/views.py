from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from produtos.models import Produto, EstoqueProduto


class IndexView(generic.ListView):
    template_name = 'produtos/index.html'
    context_object_name = 'latest_products'

    def get_queryset(self):
        return Produto.objects.order_by('data_cadastro')[:5]


class DetailView(generic.DetailView):
    model = Produto
    template_name = 'produtos/detail.html'


class ResultsView(generic.DetailView):
    model = Produto
    template_name = 'produtos/results.html'


def produtos(request, tipo_produto):
    estoques = EstoqueProduto.objects.filter(
        produto__tipo__mnemonico=tipo_produto
    )
    return render(request, 'produtos/produtos.html', {
        'estoques': estoques
    })


def estoque(request, produto_id):
    return HttpResponse("Estoque do produto %s." % produto_id)


def comprar(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    session_key = request.session.session_key

    carrinho = cache.get(session_key, {})
    if carrinho.get(produto_id):
        carrinho[produto_id] = carrinho.get(produto_id) + 1
    else:
        carrinho[produto_id] = 1
    cache.set(session_key, carrinho)
    return HttpResponseRedirect(reverse('produtos:list_produtos', args=(produto.tipo.mnemonico,)))
