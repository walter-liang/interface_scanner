# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-02 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfacescanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='postdata',
            field=models.CharField(default='', max_length=200, verbose_name='post\u53c2\u6570'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='proxy',
            field=models.CharField(default='', max_length=20, verbose_name='\u4ee3\u7406\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='station',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='interfacescanner.Station', verbose_name='\u5b9e\u9645\u72b6\u6001'),
        ),
    ]
