# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_estoqueproduto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueproduto',
            name='tamanho',
            field=models.IntegerField(choices=[(16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23')], null=True),
        ),
    ]
