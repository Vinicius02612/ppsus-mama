def  calcular_predicao(sexo,idade,temcancer,cancer_mama, idade_diagnostico,mutacaoGenetica,opc_bilateral,opc_ovario,tipo_molecular,tam_cancer,historicoFMasculino,qtd_parent_1,qtd_parent_2,parent_seg_grau,parent_pri_grau,asc_judia):
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

    
    if mutacaoGenetica in ["BRCA1", "BRCA2", "CDH1", "STK11", "PTEN", "PALB2", "VUS"]:
        peso_mutacao = 9
    else:
        peso_mutacao = 0
    
    print(peso_mutacao)

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

    print(peso_temcancer)
    print(peso_mutacaoGenetica)
    print(peso_opc_bilateral)
    print(peso_opc_ovario)
    print(peso_historicoFMasculino)
    print(peso_asc_judia)

    
    if idade_diagnostico in ["Maior que 60 anos", "Entre 55 e 60 anos", "Entre 45 e 55 anos", "Entre 35 e 44 anos", "Entre 30 e 34 anos", "Menor que 30 anos"]:
            peso_idade_diagnostico = 1
    else:
            peso_idade_diagnostico = 2
    
    print(peso_idade_diagnostico)

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
    
    print(peso_cancer_mama)
          
    """ Quantidade parentes de primeiro e (segundo < idade menor que 50) grau com câncer de mama: """
    if qtd_parent_1 == "Um" and qtd_parent_2 == "um":
        peso_qtd_parent_1 = 1
        peso_qtd_parent_2 = 1
    elif qtd_parent_1 ==  "Dois" and qtd_parent_2 == "Dois":
        peso_qtd_parent_1 = 2
        peso_qtd_parent_2 = 2
    elif qtd_parent_1 == "Três" and qtd_parent_1 == "Três":
        peso_qtd_parent_1 = 2
        peso_qtd_parent_2 = 2
    else:
        peso_qtd_parent_1 = 0
        peso_qtd_parent_2 = 0
    
    print(peso_qtd_parent_1)
    print(peso_qtd_parent_2)

    
    if parent_seg_grau == "Um":
        peso_parent_seg_grau = 1
    elif parent_seg_grau == "Dois":
        peso_parent_seg_grau = 2
    elif parent_seg_grau == "Três":
        peso_parent_seg_grau = 2
    else:
         peso_parent_seg_grau = 0
    
    print(peso_parent_seg_grau)

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
    

    print(peso_tam_cancer)
    
    print(parent_pri_grau)

    #verificar se todas os campos foram marcados, se foram todos marcados
    #a multiplcação do peso pela quantidade deve ser 12, pois 6 * 2 = 12
    #caso sejam marcadas menos opçoes que o tatol deve se saber quais foram e multiplicar os valores de cada opção.
    for i in parent_pri_grau:
        if i == "Cancer de ovario"\
            or i == "Cancer de mama masculino"\
            or i == "Cancer de prostata"\
            or i == "Cancer bilateral de mama"\
            or i == "Cancer de pancreas":
            peso_parent_pri_grau = 2
        else:
            peso_parent_pri_grau = 0
    pontuacao = (peso_parent_pri_grau+peso_tam_cancer+peso_parent_seg_grau+peso_qtd_parent_2+peso_qtd_parent_1+peso_cancer_mama+peso_temcancer+peso_temcancer+peso_mutacao+peso_opc_bilateral+peso_mutacaoGenetica+peso_opc_ovario+peso_historicoFMasculino+peso_asc_judia+peso_idade_diagnostico+peso_tipo_molecular)
    
   

    print(pontuacao)
    

    return pontuacao
    

    

    


