# Generated by Django 3.2.5 on 2023-05-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20230530_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='temcancer',
            field=models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], max_length=3, verbose_name='Tem câncer de mama?'),
        ),
    ]