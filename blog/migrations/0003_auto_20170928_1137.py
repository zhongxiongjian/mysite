# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170928_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='addr',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='qq',
            field=models.CharField(max_length=10),
        ),
    ]
