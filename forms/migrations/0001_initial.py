# Generated by Django 3.2.5 on 2023-06-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePaciente', models.CharField(blank=True, max_length=255, verbose_name='Nome do paciente:')),
                ('sobrenome', models.CharField(blank=True, max_length=255, verbose_name='Sobrenome:')),
                ('nomeclinica', models.CharField(blank=True, max_length=255, verbose_name='Nome da clinica:')),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=2, verbose_name='Sexo')),
                ('idadepaciente', models.CharField(max_length=3, verbose_name='Idade do paciente:')),
                ('temcancer', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], max_length=3, verbose_name='Tem câncer de mama?')),
                ('cancer_mama', models.CharField(choices=[('Carcinoma ductal insitu', 'Carcinoma ductal insitu'), ('Carcinoma não epecial', 'Carcinoma não epecial'), ('Lobural', 'Lobural'), ('Medular', 'Medular'), ('Metaplatico', 'Metaplatico'), ('Mucinoso', 'Mucinoso'), ('Não tem cancer de mama', 'Não tem cancer de mama')], max_length=25, verbose_name='Se tem câncer de mama, qual tipo histologico?')),
                ('idade_diagnostico', models.CharField(choices=[('Maior que 60 anos', 'Maior que 60 anos'), ('Entre 55 e 60 anos', 'Entre 55 e 60 anos'), ('Entre 45 e 55 anos', 'Entre 45 e 55 anos'), ('Entre 35 e 45 anos', 'Entre 35 e 45 anos'), ('Entre 30 e 35 anos', 'Entre 30 e 35 anos'), ('Menor que 30 anos', 'Menor que 30 anos'), ('Menor que 30 anos', 'Menor que 30 anos'), ('Sem diagnostico', 'Sem diagnostico')], max_length=25, verbose_name='Faixa de idade do diagnostico de câncer de mama:')),
                ('mutacaoGenetica', models.CharField(choices=[('BRCA1', 'BRCA1'), ('BRCA2', 'BRCA2'), ('TP53', 'TP53'), ('CDH1', 'CDH1'), ('STK11', 'STK11'), ('PTEN', 'PTEN'), ('PALB2', 'PALB2'), ('VUS', 'VUS'), ('NÃO APRESENTA MUTAÇÃO', 'NÃO APRESENTA MUTAÇÃO')], max_length=22, verbose_name='Teste genético apresenta mutação do tipo:')),
                ('opc_bilateral', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], max_length=3, verbose_name='Historico Pessoal de cancer de mama bilateral:')),
                ('opc_ovario', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], max_length=3, verbose_name='Tem historico Pessoal de cançer de ovario?')),
                ('tipo_molecular', models.CharField(choices=[('Luminal', 'Luminal'), ('Luminal HEr2', 'Luminal HEr2'), ('HEr2', 'HEr2'), ('Triplo Negativo', 'Triplo Negativo'), ('Não tem cancer de mama', 'Não tem cancer de mama')], max_length=23, verbose_name='Tipo molecular de câncer de mama:')),
                ('tam_cancer', models.CharField(choices=[('Insitu', 'Insitu'), ('T1', 'T1'), ('T2', 'T2'), ('T3', 'T3'), ('T4', 'T4'), ('Não tem cancer de mama', 'Não tem cancer de mama')], max_length=23, verbose_name='Se tem câncer, qual o tamanho do tumor:')),
                ('qtd_parent_1', models.CharField(choices=[('Um', 'Um'), ('Dois', 'Dois'), ('Três ou Mais', 'Três ou Mais'), ('Desconhece', 'Desconhece')], max_length=12, verbose_name='Quantidade parentes de primeiro grau com câncer de mama:')),
                ('qtd_parent_2', models.CharField(choices=[('Um', 'Um'), ('Dois', 'Dois'), ('Três ou Mais', 'Três ou Mais'), ('Desconhece', 'Desconhece')], max_length=12, verbose_name=' Quantidade de parentes de primeiro grau ou mais distante com câncer de mama ou ovario com idade  < 50 anos')),
                ('parent_seg_grau', models.CharField(choices=[('Um', 'Um'), ('Dois', 'Dois'), ('Três ou Mais', 'Três ou Mais'), ('Desconhece', 'Desconhece')], max_length=12, verbose_name='Quantidade parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:')),
                ('parent_pri_grau', models.CharField(choices=[('Cancer de ovario', 'Cancer de ovario'), ('Cancer de mama masculino', 'Cancer de mama masculino'), ('Cancer de prostata', 'Cancer de prostata'), ('Cancer bilateral de mama', 'Cancer bilateral de mama'), ('Cancer de pancreas', 'Cancer de pancreas'), ('Dois ou mais itens', 'Dois ou mais itens'), ('Nenhum', 'Nenhum'), ('Desconhce', 'Desconhece')], max_length=25, verbose_name='Parentes de primeiro grau com :')),
                ('asc_judia', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NAO')], max_length=12, verbose_name='Ascendencia Judia Ashkenazi:')),
            ],
        ),
    ]