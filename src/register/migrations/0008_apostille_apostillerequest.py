# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20160318_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apostille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placing_date', models.DateField(verbose_name='Placing date')),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='register.Document')),
                ('validator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ApostilleRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Applicant', models.CharField(max_length=150)),
                ('receiving_date', models.DateTimeField(verbose_name='Receiving Date')),
                ('payment_file', models.FileField(upload_to='payments/')),
                ('is_open', models.BooleanField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Department')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Document')),
            ],
        ),
    ]
