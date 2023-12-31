# Generated by Django 4.2.5 on 2023-11-13 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartattendance', '0004_alter_presenca_tempo_entrada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno_turma',
            old_name='aluno_id',
            new_name='aluno',
        ),
        migrations.RenameField(
            model_name='aluno_turma',
            old_name='turma_id',
            new_name='turma',
        ),
        migrations.RenameField(
            model_name='chamada',
            old_name='turma_id',
            new_name='turma',
        ),
        migrations.RenameField(
            model_name='presenca',
            old_name='aluno_id',
            new_name='aluno',
        ),
        migrations.RenameField(
            model_name='presenca',
            old_name='chamada_id',
            new_name='chamada',
        ),
        migrations.RenameField(
            model_name='turma',
            old_name='professor_id',
            new_name='professor',
        ),
        migrations.RenameField(
            model_name='turma_horario',
            old_name='turma_id',
            new_name='turma',
        ),
    ]
