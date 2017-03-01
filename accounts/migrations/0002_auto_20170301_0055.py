# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 03:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clienteuser',
            old_name='dia_nascimento',
            new_name='data_nascimento',
        ),
        migrations.AddField(
            model_name='clienteuser',
            name='nome',
            field=models.CharField(default=datetime.datetime(2017, 3, 1, 3, 55, 35, 852970, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clienteuser',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]