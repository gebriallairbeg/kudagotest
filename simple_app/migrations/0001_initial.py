# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('persons', models.CharField(blank=True, max_length=200, null=True)),
                ('image_source', models.CharField(blank=True, max_length=255, null=True)),
                ('resource_url', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Event will be go on around')),
                ('legal_age', models.IntegerField(blank=True, null=True, verbose_name='It is forbidden to visit before')),
                ('price_min', models.FloatField(blank=True, null=True)),
                ('price_max', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('image_source', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=50, null=True)),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField(blank=True, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='simple_app.Event')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='simple_app.Place')),
            ],
        ),
    ]