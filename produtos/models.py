from django.db import models



class TipoProduto(models.Model):
    mnemonico = models.CharField(max_length=100)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    descricao = models.CharField(max_length=200)
    data_cadastro = models.DateTimeField('Data de cadastro')
    path_imagem = models.CharField(max_length=500)
    tipo = models.ForeignKey(TipoProduto)

    def __str__(self):
        return self.descricao


class EstoqueProduto(models.Model):
    quantidade = models.IntegerField()
    TAMANHOS_DISPONIVEIS = (
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
    )
    tamanho = models.IntegerField(choices=TAMANHOS_DISPONIVEIS)
    produto = models.ForeignKey(Produto)

    def __str__(self):
        return '{} - Quantidade: {} - Tamanho: {}'.format(self.produto.descricao, self.quantidade, self.tamanho)

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    path_imagem = models.CharField(max_length=500)
