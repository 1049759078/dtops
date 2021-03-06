# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-30 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_delete_salt_returns'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, 'zookeeper'), (2, 'nginx'), (3, 'redis'), (4, 'mysql')], default='模块名称', max_length=30)),
                ('deploy', models.CharField(default='备注', max_length=100)),
                ('host', models.ForeignKey(default='主机节点', on_delete=django.db.models.deletion.CASCADE, to='tasks.KeyList')),
            ],
            options={
                'verbose_name_plural': '模块部署',
                'verbose_name': '模块部署',
            },
        ),
    ]
