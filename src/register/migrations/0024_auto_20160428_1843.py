# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-28 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0023_auto_20160428_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostille',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.ApostilleRequest'),
        ),
    ]