# Generated by Django 4.0.1 on 2022-01-18 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('tipo_despesa', models.CharField(max_length=3)),
                ('valor', models.FloatField()),
                ('vencimento_fatura', models.DateField(default=django.utils.timezone.now)),
                ('status_pagamento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inquilinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.CharField(max_length=3)),
                ('sexo', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identicacao', models.CharField(max_length=255)),
                ('proprietario', models.CharField(max_length=3)),
                ('condominio', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=15)),
            ],
        ),
    ]
