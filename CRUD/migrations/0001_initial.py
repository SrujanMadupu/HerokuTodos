# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastdate', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
            ],
        ),
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask', models.CharField(max_length=200)),
                ('length', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.Todo')),
            ],
        ),
    ]
