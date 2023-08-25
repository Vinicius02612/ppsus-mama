from  django import forms

class Questionario(forms.Form):

    
    nomePaciente = forms.CharField(label="Nome do paciente:",max_length=255, required=False)
    sobrenome = forms.CharField(label="Sobrenome:",max_length=255,required=False)
    nomeclinica =  forms.CharField(label="Nome da clinica:",max_length=255,required=False)

    tuplesexo = (
        ("",""),
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    sexo = forms.ChoiceField(label="Sexo", choices=tuplesexo)
    idadepaciente =  forms.CharField(label="Idade do paciente:",required=True)

    tupleOpcao = (
        ("",""),
        ("SIM", "SIM"),
        ("NAO", "NAO"),
    )
    temcancer = forms.ChoiceField(label="Tem câncer de mama?",choices=tupleOpcao)

    tupleCancer = (
        ("",""),
        ("Carcinoma ductal insitu", "Carcinoma ductal insitu"),
        ("Carcinoma ductal invasivo", "Carcinoma ductal invasivo"),
        ("Lobural", "Lobural"),
        ("Medular", "Medular"),
        ("Metaplatico", "Metaplatico"),
        ("Mucinoso", "Mucinoso"),
        ("Não tem câncer de mama", "Não tem câncer de mama"),
        ("Sem informação", "Sem informação"),
    )

    cancer_mama = forms.ChoiceField(label="Se tem câncer de mama, qual tipo histologico?",choices=tupleCancer)

    tupleTipoMolecular = (
        ("",""),
        ("Luminal", "Luminal"),
        ("Luminal HEr2", "Luminal HEr2"),
        ("HEr2", "HEr2"),
        ("Triplo Negativo", "Triplo Negativo"),
        ("Não tem câncer de mama", "Não tem câncer de mama"),
        ("Sem informação", "Sem informação"),

    )

    tipo_molecular = forms.ChoiceField(label="Tipo molecular de câncer de mama:",choices=tupleTipoMolecular)
    
    tupleIdadeCancer = (
        ("",""),
        ("Maior que 60 anos","Maior que 60 anos"),
        ("Entre 55 e 60 anos", "Entre 55 e 60 anos"),
        ("Entre 45 e 54 anos", "Entre 45 e 54 anos"),
        ("Entre 35 e 44 anos", "Entre 35 e 44 anos"),
        ("Entre 30 e 34 anos", "Entre 30 e 34 anos"),
        ("Menor que 30 anos", "Menor que 30 anos"),
        ("Sem diagnostico", "Sem diagnostico"),  
    )
    idade_diagnostico =  forms.ChoiceField(label="Faixa de idade do diagnostico de câncer de mama:" ,choices=tupleIdadeCancer)

    tupleMutacao = (
        ("",""),
        ("BRCA1", "BRCA1"),
        ("BRCA2", "BRCA2"),
        ("TP53", "TP53"),
        ("CDH1", "CDH1"),
        ("STK11", "STK11"), 
        ("PTEN", "PTEN"),
        ("PALB2","PALB2"),
        ("VUS", "VUS"),
        ("Não apresenta mutação", "Não apresenta mutação"),
        ("Sem informação", "Sem informação"),
    )
    mutacaoGenetica =  forms.ChoiceField(label="Teste genético apresenta mutação do tipo:", choices=tupleMutacao)
    opc_bilateral = forms.ChoiceField(label="Historico Pessoal de câncer de mama bilateral:", choices=tupleOpcao)
    opc_ovario = forms.ChoiceField(label="Tem historico Pessoal de câncer de ovario?", choices=tupleOpcao)

    

    tupleTamanhoDoCancer = (
        ("",""),
        ("Insitu", "Insitu"),
        ("T1", "T1"),
        ("T2", "T2"),
        ("T3", "T3"),
        ("T4", "T4"),
        ("Não tem câncer de mama", "Não tem câncer de mama"),
        ("Sem informação", "Sem informação"),

    )
    tam_cancer = forms.ChoiceField(label="Se tem câncer, qual o tamanho do tumor:",choices=tupleTamanhoDoCancer)
    
    tupleQtdParente = (
        ("",""),
        ("Um", "Um"),
        ("Dois", "Dois"),
        ("Três ou Mais", "Três ou Mais"),
        ("Desconhece", "Desconhece"),
        ("Nenhum", "Nenhum"),
    )

    historicoFMasculino =  forms.ChoiceField(label="Histórico familiar de câncer de mama masculino da familia ?", choices=tupleOpcao)
    qtd_parent_2 = forms.ChoiceField(label=" Quantidade de parentes de primeiro grau com câncer de mama ou ovario com idade  < 50 anos",choices=tupleQtdParente)
    parent_seg_grau =  forms.ChoiceField(label="Quantidade parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:",choices=tupleQtdParente)


    parent_pri_grau =  forms.MultipleChoiceField(label="Parentes de primeiro grau com :",
                                                choices=[
                                                        ("Câncer de mama", "Câncer de mama"),
                                                        ("Câncer de ovario", "Câncer de ovario"),
                                                        ("Câncer de mama masculino", "Câncer de mama masculino"),
                                                        ("Câncer de prostata", "Câncer de prostata"),
                                                        ("Câncer bilateral de mama", "Câncer bilateral de mama"),
                                                        ("Câncer de pancreas", "Câncer de pancreas"),
                                                        ("Não tem câncer","Não tem câncer"),
                                                        ("Sem informação", "Sem informação")],
                                                widget=forms.CheckboxSelectMultiple,
    )
    asc_judia =  forms.ChoiceField(label="Ascendencia Judia Ashkenazi:",choices=tupleOpcao)





