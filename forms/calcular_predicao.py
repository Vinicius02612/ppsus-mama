def  calcular_predicao(sexo,idade,temcancer,cancer_mama, idade_diagnostico,mutacaoGenetica,opc_bilateral,opc_ovario,tipo_molecular,tam_cancer,historicoFMasculino,qtd_parent_2,parent_seg_grau,parent_pri_grau,asc_judia):
    """ Esta função faz o calculo da predição com base nas respostas fornecidas pelo usuário e retora o resultado """
    """ Terminar de fazer o restante dos pesos das outras opções """
    peso_mutacao = 0
    peso_temcancer = 0
    peso_mutacaoGenetica = 0
    peso_opc_bilateral = 0
    peso_opc_ovario = 0
    peso_historicoFMasculino = 0
    peso_asc_judia = 0
    peso_idade_diagnostico = 0
    peso_tipo_molecular = 0
    peso_cancer_mama = 0
    peso_qtd_parent_1 = 0
    peso_qtd_parent_2 = 0
    peso_parent_seg_grau = 0
    peso_tam_cancer = 0


    pesoMaximo_total_cancer = 2
    pesoMaximo_tam_cancer = 5 
    pesoMaximo_parent_seg_grau = 2
    pesoMaximo_qtd_parent_2 = 3
    pesoMaximo_cancer_mama = 5
    pesoMaximo_temcancer = 1
    pesoMaximo_mutacao = 9
    pesoMaximo_opc_bilateral = 5
    pesoMaximo_mutacaoGenetica = 1
    pesoMaximo_opc_ovario= 5
    pesoMximo_historicoFMasculino = 1
    pesoMaximo_asc_judia = 9
    pesoMaximo_idade_diagnostico = 2
    pesoMaximo_tipo_molecular = 5


    
    if mutacaoGenetica in ["BRCA1", "BRCA2", "CDH1", "STK11", "PTEN", "PALB2", "VUS"]:
        peso_mutacao = 9
    else:
        peso_mutacao = 0

    if temcancer == "sim"\
        and mutacaoGenetica =="sim"\
        and opc_bilateral == "sim"\
        and opc_ovario == "sim"\
        and historicoFMasculino == "sim"\
        and asc_judia == "sim":
            peso_temcancer = 1
            peso_mutacaoGenetica = 1
            peso_opc_bilateral = 5
            peso_opc_ovario = 5
            peso_historicoFMasculino = 1
            peso_asc_judia = 9
    else:
            peso_temcancer = 0
            peso_mutacaoGenetica = 0
            peso_opc_bilateral = 0
            peso_opc_ovario = 0
            peso_historicoFMasculino = 0
            peso_asc_judia = 0

   
    if idade_diagnostico in ["Maior que 60 anos", "Entre 55 e 60 anos", "Entre 45 e 55 anos", "Entre 35 e 44 anos", "Entre 30 e 34 anos", "Menor que 30 anos"]:
            peso_idade_diagnostico = 2
    else:
            peso_idade_diagnostico = 0
    


    """ "Tipo molecular de câncer de mama: """
    if tipo_molecular == "Triplo Negativo":
        peso_tipo_molecular = 5
    else:
        peso_tipo_molecular = 0
    
    print(peso_tipo_molecular)
    """ Se tem câncer de mama, qual tipo histologico? """
    if cancer_mama == "Carcinoma ductal insitu":
        peso_cancer_mama = 5
    elif cancer_mama == "Carcinoma ductal invasivo":
        peso_cancer_mama = 4
    elif cancer_mama == "Lobural":
        peso_cancer_mama = 3
    elif cancer_mama == "Metaplatico":
        peso_cancer_mama = 2
    elif cancer_mama =="Mucinoso":
        peso_cancer_mama = 1
    else:
        peso_cancer_mama = 0
    
          
    """ Quantidade parentes de primeiro e (segundo < idade menor que 50) grau com câncer de mama: """
    if qtd_parent_2 == "um":
        peso_qtd_parent_2 = 1
    elif qtd_parent_2 == "Dois":
        peso_qtd_parent_2 = 2
    elif qtd_parent_2 == "Três":
        peso_qtd_parent_2 = 3
    else:
        peso_qtd_parent_2 = 0
    
    
    if parent_seg_grau == "Um":
        peso_parent_seg_grau = 1
    elif parent_seg_grau == "Dois":
        peso_parent_seg_grau = 2
    elif parent_seg_grau == "Três":
        peso_parent_seg_grau = 2
    else:
         peso_parent_seg_grau = 0
    


    if tam_cancer == "Insitu":
        peso_tam_cancer = 5
    elif tam_cancer == "T1":
        peso_tam_cancer = 1
    elif tam_cancer == "T2":
        peso_tam_cancer = 2
    elif tam_cancer == "T3":
        peso_tam_cancer = 3
    elif tam_cancer == "T4":
        peso_tam_cancer = 4
    else:
        peso_tam_cancer = 0

    pesos_opcoes = {
        "Cancer de ovario": 2,
        "Cancer de mama masculino": 2,
        "Cancer de prostata": 2,
        "Cancer bilateral de mama": 2,
        "Cancer de pancreas": 2,
        "Não tem cancer": 0,
    }
    peso_total_cancer = 0
    for i in parent_pri_grau:
        if i in pesos_opcoes:
            peso_total_cancer += pesos_opcoes[i]
        else:
            peso_total_cancer = 0

    valor_maximo_pesos = (pesoMaximo_total_cancer+ pesoMaximo_tam_cancer + pesoMaximo_parent_seg_grau + pesoMaximo_qtd_parent_2 + pesoMaximo_cancer_mama +  pesoMaximo_temcancer + pesoMaximo_mutacao + pesoMaximo_opc_bilateral + pesoMaximo_mutacaoGenetica + pesoMaximo_opc_ovario +pesoMximo_historicoFMasculino+pesoMaximo_asc_judia + pesoMaximo_idade_diagnostico +pesoMaximo_tipo_molecular ) 
    pontuacao = (peso_total_cancer+peso_tam_cancer+peso_parent_seg_grau+peso_qtd_parent_2+peso_qtd_parent_1+peso_cancer_mama+peso_temcancer+peso_mutacao+peso_opc_bilateral+peso_mutacaoGenetica+peso_opc_ovario+peso_historicoFMasculino+peso_asc_judia+peso_idade_diagnostico+peso_tipo_molecular)

    porcentagem = (pontuacao/valor_maximo_pesos)*100
    porcentagem_arredondado = round(porcentagem, 2)
    return porcentagem_arredondado
    

    

    


