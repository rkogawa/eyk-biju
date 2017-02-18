from django.core.cache import cache
from django.shortcuts import render

from pagamentos.forms import CalcularFreteForm
from pagamentos.models import CompraItem
from produtos.models import EstoqueProduto


def carrinho(request, **kwargs):
    session_key = request.session.session_key
    carrinho = cache.get(session_key, {})
    compras = []
    for estoque_id, quantidade in carrinho.items():
        compras.append(CompraItem(
            item=EstoqueProduto.objects.get(pk=estoque_id),
            quantidade=quantidade,
        ))

    return render(request, 'pagamentos/carrinho.html', {
        'compras': compras,
        **kwargs,
    })


def calcular_frete(request):
    if request.method == 'POST':
        form = CalcularFreteForm(request.POST)
        if form.is_valid():
            return carrinho(request, **form.calcular_frete())
    return carrinho(request)