# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_app.Event'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simple_app.Place'),
        ),
    ]
