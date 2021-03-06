# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_temperature', models.FloatField(verbose_name='Max Temperature')),
                ('min_temperature', models.FloatField(verbose_name='Max Temperature')),
                ('mean_temperature', models.FloatField(verbose_name='Max Temperature')),
                ('sunshine', models.FloatField(verbose_name='Sunshine')),
                ('rainfall', models.FloatField(verbose_name='Rainfall')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
            ],
            options={
                'db_table': 'monthly_weather',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.AddField(
            model_name='monthlyweather',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_weather', to='weather_data.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='monthlyweather',
            unique_together=set([('month', 'year', 'region')]),
        ),
    ]
