# Generated by Django 3.2.5 on 2023-04-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20230417_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='idadepaciente',
            field=models.CharField(max_length=3, verbose_name='Idade do paciente:'),
        ),
    ]
