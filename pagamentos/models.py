from django.db import models

from produtos.models import Produto, EstoqueProduto


class CompraItem(models.Model):
    item = models.ForeignKey(EstoqueProduto)
    quantidade = models.IntegerField()

    @property
    def valor_total(self):
        return self.quantidade * self.item.preco
