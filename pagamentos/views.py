from django.core.cache import cache
from django.shortcuts import render

from pagamentos.models import CompraItem
from produtos.models import EstoqueProduto


def carrinho(request):
    session_key = request.session.session_key
    carrinho = cache.get(session_key, {})
    compras = []
    for estoque_id, quantidade in carrinho.items():
        compras.append(CompraItem(
            item=EstoqueProduto.objects.get(pk=estoque_id),
            quantidade=quantidade,
        ))
    return render(request, 'pagamentos/carrinho.html', {
        'compras': compras
    })
