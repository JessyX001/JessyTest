# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-17 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phoneinfo', '0005_auto_20181016_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='phoneinfo',
            name='pic_url',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u56fe\u7247\u4e0a\u4f20\u8def\u5f84'),
        ),
    ]