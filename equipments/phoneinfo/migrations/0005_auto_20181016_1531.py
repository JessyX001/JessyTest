# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-16 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneinfo', '0004_auto_20181016_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneinfo',
            name='status',
            field=models.IntegerField(choices=[(0, '\u672a\u501f\u51fa'), (1, '\u5df2\u501f\u51fa')], default=0),
        ),
    ]