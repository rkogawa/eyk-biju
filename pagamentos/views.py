from decimal import Decimal
from django.core.cache import cache
from django.shortcuts import render

from pagamentos.forms import CalcularFreteForm
from pagamentos.models import CompraItem
from produtos.models import EstoqueProduto


def carrinho(request, **kwargs):
    session_key = request.session.session_key
    carrinho = cache.get(session_key, {})
    compras = []

    valor_compras = 0
    for estoque_id, quantidade in carrinho.items():
        item = CompraItem(
            item=EstoqueProduto.objects.get(pk=estoque_id),
            quantidade=quantidade,
        )
        valor_compras += item.valor_total
        compras.append(item)

    for fretes in kwargs.get('fretes', []):
        if fretes.get('Codigo') == kwargs.get('tipo_frete'):
            kwargs['valor_frete'] = Decimal(fretes.get('Valor').replace(',', '.'))
    return render(request, 'pagamentos/carrinho.html', {
        'compras': compras,
        'valor_compras': valor_compras,
        'valor_total': valor_compras + kwargs.get('valor_frete', 0),
        **kwargs,
    })


def calcular_frete(request):
    if request.method == 'POST':
        form = CalcularFreteForm(request.POST)
        if form.is_valid():
            return carrinho(request, **form.calcular_frete())
    return carrinho(request)
