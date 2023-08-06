from django import forms

class Questions(forms.Form):
    nomePaciente1 = forms.CharField(label="Nome do paciente:", required=False)
    sobrenome = forms.CharField(label="Sobrenome:",required=False)
    nomeclinica =  forms.CharField(label="Nome da clinica:",required=False)

    tuplesexo = (
        ("",""),
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    sexo = forms.ChoiceField(label="Sexo",  choices=tuplesexo )
    idadepaciente =  forms.IntegerField(label="Idade do paciente:")

    tupleOpcao = (
        ("",""),
        ("SIM", "SIM"),
        ("NAO", "NAO"),
    )
    temcancer = forms.ChoiceField(label="Tem câncer de mama?", choices=tupleOpcao)

    

    tupleCancer = (
            ("",""),
            ("Carcinoma ductal insitu", "Carcinoma ductal insitu"),
            ("Carcinoma não epecial", "Carcinoma não epecial"),
            ("Lobural", "Lobural"),
            ("Medular", "Medular"),
            ("Metaplatico", "Metaplatico"),
            ("Mucinoso", "Mucinoso"),
            ("Não tem cancer de mama", "Não tem cancer de mama"),
    )

    cancer_mama = forms.ChoiceField(label="Se tem câncer de mama, qual tipo histologico?", choices=tupleCancer, widget='')

    tupleIdadeCancer = (
        ("",""),
        ("Maior que 60 anos","Maior que 60 anos"),
        ("Entre 55 e 60 anos", "Entre 55 e 60 anos"),
        ("Entre 45 e 55 anos", "Entre 45 e 55 anos"),
        ("Entre 35 e 45 anos", "Entre 35 e 45 anos"),
        ("Entre 30 e 35 anos", "Entre 30 e 35 anos"),
        ("Menor que 30 anos", "Menor que 30 anos"),
        ("Menor que 30 anos", "Menor que 30 anos"),
        ("Sem diagnostico", "Sem diagnostico"),  


    )
    idade_diagnostico =  forms.ChoiceField(label="Faixa de idade do diagnostico de câncer de mama:",choices=tupleIdadeCancer)

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
        ("NÃO APRESENTA MUTAÇÃO", "NÃO APRESENTA MUTAÇÃO"),

    )
    mutacaoGenetica =  forms.ChoiceField(label="Teste genético apresenta mutação do tipo:",choices=tupleMutacao)

    opc_bilateral = forms.ChoiceField(label="Historico Pessoal de cancer de mama bilateral:", choices=tupleOpcao)
    opc_ovario = forms.ChoiceField(label="Tem historico Pessoal de cançer de ovario?",choices=tupleOpcao)

    tupleTipoMolecular = (
        ("",""),
        ("Luminal", "Luminal"),
        ("Luminal HEr2", "Luminal HEr2"),
        ("HEr2", "HEr2"),
        ("Triplo Negativo", "Triplo Negativo"),
        ("Não tem cancer de mama", "Não tem cancer de mama"),

    )

    tipo_molecular = forms.ChoiceField(label="Tipo molecular de câncer de mama:", choices=tupleTipoMolecular)

    tupleTamanhoDoCancer = (
        ("",""),
        ("Insitu", "Insitu"),
        ("T1", "T1"),
        ("T2", "T2"),
        ("T3", "T3"),
        ("T4", "T4"),
        ("Não tem cancer de mama", "Não tem cancer de mama"),

    )
    tam_cancer = forms.ChoiceField(label="Se tem câncer, qual o tamanho do tumor:",choices=tupleTamanhoDoCancer)
    
    tupleQtdParente = (
        ("",""),
        ("Um", "Um"),
        ("Dois", "Dois"),
        ("Três ou Mais", "Três ou Mais"),
        ("Desconhece", "Desconhece"),
    )
    qtd_parent_1 = forms.ChoiceField(label="Quantidade parentes de primeiro grau com câncer de mama:",choices=tupleQtdParente)
    
    qtd_parent_2 = forms.ChoiceField(label=" Quantidade de parentes de primeiro grau ou mais distante com câncer de mama ou ovario com idade  < 50 anos", choices=tupleQtdParente)
    

    parent_seg_grau =  forms.ChoiceField(label="Quantidade parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:", choices=tupleQtdParente)


    tupleParentePrimeiroGrau= (
        ("",""),
        ("Cancer de ovario", "Cancer de ovario"),
        ("Cancer de mama masculino", "Cancer de mama masculino"),
        ("Cancer de prostata", "Cancer de prostata"),
        ("Cancer bilateral de mama", "Cancer bilateral de mama"),
        ("Cancer de pancreas", "Cancer de pancreas"),
        ("Dois ou mais itens", "Dois ou mais itens"),
        ("Nenhum", "Nenhum"),
        ("Desconhce","Desconhece")

    )
    parent_pri_grau =  forms.ChoiceField(label="Parentes de primeiro grau com :",choices=tupleParentePrimeiroGrau)

    asc_judia =  forms.ChoiceField(label="Ascendencia Judia Ashkenazi:",choices=tupleOpcao)

        

