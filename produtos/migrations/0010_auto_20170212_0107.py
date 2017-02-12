# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_estoqueproduto_preco_sem_desconto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueproduto',
            name='preco_sem_desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='estoqueproduto',
            name='tamanho',
            field=models.IntegerField(blank=True, choices=[(16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23')], null=True),
        ),
    ]
