# Generated by Django 4.2.6 on 2023-10-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartattendance', '0002_alter_turma_horario_hora_fim_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamada',
            name='raio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='presenca',
            name='caminho_atestado',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='presenca',
            name='status',
            field=models.CharField(choices=[('P', 'Presente'), ('F', 'Falta'), ('C', 'Contestação')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='presenca',
            name='ultima_atualizacao',
            field=models.DateTimeField(null=True),
        ),
    ]
