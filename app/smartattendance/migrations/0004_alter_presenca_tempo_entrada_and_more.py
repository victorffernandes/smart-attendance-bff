# Generated by Django 4.2.5 on 2023-11-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartattendance', '0003_chamada_raio_presenca_caminho_atestado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='tempo_entrada',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='tempo_saida',
            field=models.DateTimeField(null=True),
        ),
    ]
