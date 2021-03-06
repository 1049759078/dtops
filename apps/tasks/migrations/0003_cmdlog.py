# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-27 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180414_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='CmdLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=30, null=True, verbose_name='目标主机')),
                ('cmd', models.CharField(blank=True, max_length=100, null=True, verbose_name='执行命令')),
                ('user', models.CharField(blank=True, max_length=20, null=True, verbose_name='执行用户')),
                ('set_time', models.DateTimeField(auto_now_add=True, verbose_name='执行时间')),
            ],
            options={
                'verbose_name_plural': '执行命令记录',
                'verbose_name': '执行命令记录',
            },
        ),
    ]
