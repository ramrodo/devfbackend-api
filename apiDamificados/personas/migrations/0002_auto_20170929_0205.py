# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
