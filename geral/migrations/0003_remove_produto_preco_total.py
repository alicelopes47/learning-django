# Generated by Django 4.2.7 on 2023-11-24 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0002_produto_preco_produto_preco_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_total',
        ),
    ]
