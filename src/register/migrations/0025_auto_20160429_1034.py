# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-29 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0024_auto_20160428_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='code',
        ),
        migrations.AddField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
