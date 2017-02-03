from django.contrib import admin

from .models import Produto, TipoProduto, EstoqueProduto

admin.site.register(Produto)
admin.site.register(EstoqueProduto)
admin.site.register(TipoProduto)