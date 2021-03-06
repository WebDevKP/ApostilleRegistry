# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_apostille_apostillerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apostillerequest',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.Document'),
        ),
        migrations.AlterField(
            model_name='apostillerequest',
            name='payment_file',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='signet',
            name='sign',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='signet',
            name='stamp',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
