def  calcular_predicao(sexo,idade,temcancer,cancer_mama, idade_diagnostico,mutacaoGenetica,opc_bilateral,opc_ovario,tipo_molecular,tam_cancer,historicoFMasculino,qtd_parent_1,qtd_parent_2,parent_seg_grau,parent_pri_grau,asc_judia):
    """ Esta função faz o calculo da predição com base nas respostas fornecidas pelo usuário e retora o resultado """
    """ Terminar de fazer o restante dos pesos das outras opções """
    pontuacao,pesosexo ,peso_temcancer,peso_cancer_mama,peso_idade_diagnostico,peso_mutacao,peso_opc_bilateral,peso_opc_ovario, \
    peso_tipo_molecular,peso_tam_cancer,peso_historicoFMasculino,peso_qtd_parent_1,peso_qtd_parent_2,peso_parent_seg_grau,peso_asc_judia,peso_mutacaoGenetica

    if temcancer == "sim" and mutacaoGenetica =="sim" and opc_bilateral == "sim" and opc_ovario == "sim" and historicoFMasculino == "sim":
        peso_temcancer = 1
        peso_mutacaoGenetica = 1
        peso_opc_bilateral = 5
        peso_opc_ovario = 5
        peso_historicoFMasculino = 1
    else:
        peso_temcancer = 0
        peso_mutacaoGenetica = 0
        peso_opc_bilateral = 0
        peso_opc_ovario = 0
        peso_historicoFMasculino = 0
    
    if idade_diagnostico == "Maior que 60 anos"\
        or idade_diagnostico == "Entre 55 e 59 anos"\
        or idade_diagnostico == "Entre 45 e 54 anos"\
        or idade_diagnostico == "Entre 35 e 44 anos"\
        or idade_diagnostico == "Entre 30 e 34 anos":
        peso_idade_diagnostico = 1
    else:
        peso_idade_diagnostico = 2

    
    if tipo_molecular == "Triplo Negativo":
        peso_tipo_molecular = 5
    else:
        peso_tipo_molecular = 0

    
    

    


