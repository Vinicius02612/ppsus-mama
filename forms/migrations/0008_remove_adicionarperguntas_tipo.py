# Generated by Django 3.2.5 on 2023-08-05 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_alter_formulario_nova_pergunta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adicionarperguntas',
            name='tipo',
        ),
    ]