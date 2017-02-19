# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirBNB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airports', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=200)),
                ('adults', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=3)),
                ('destination', models.CharField(max_length=3)),
                ('date', models.DateField()),
                ('adults', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('time', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('adults', models.IntegerField()),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoFlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
    ]