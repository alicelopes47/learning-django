# Generated by Django 4.2.7 on 2023-11-24 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0003_remove_produto_preco_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.CharField(max_length=30),
        ),
    ]
