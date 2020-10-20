# Generated by Django 3.0.5 on 2020-10-19 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201016_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='cod_agendamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Agendamento'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='cod_func',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
