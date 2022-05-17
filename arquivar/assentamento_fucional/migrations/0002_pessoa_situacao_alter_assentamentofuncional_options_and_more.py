# Generated by Django 4.0.4 on 2022-05-11 23:47

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assentamento_fucional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('aniversario', models.DateField(verbose_name='Aniversário')),
                ('cpf', cpf_field.models.CPFField(blank=True, max_length=14, null=True, verbose_name='cpf')),
                ('rg', models.CharField(blank=True, max_length=14, null=True, verbose_name='RG')),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Situações',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterModelOptions(
            name='assentamentofuncional',
            options={'ordering': ['servidor'], 'verbose_name_plural': 'Assentamentos Funcionais'},
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula SIAPE')),
                ('categoria_funcional', models.CharField(choices=[('Téc_Admin', 'Tecnico Administrativo'), ('Docente', 'Docente')], max_length=10, verbose_name='Categoria')),
                ('nome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento_fucional.pessoa', verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Servidores',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='assentamentofuncional',
            name='situacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento_fucional.situacao', verbose_name='Situação Servidor'),
        ),
        migrations.AlterField(
            model_name='assentamentofuncional',
            name='servidor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assentamento_fucional.servidor', verbose_name='Nome Servidor'),
        ),
    ]