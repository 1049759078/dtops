# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-14 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keylist',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='key名'),
        ),
    ]
