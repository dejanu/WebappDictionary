# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictword',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
