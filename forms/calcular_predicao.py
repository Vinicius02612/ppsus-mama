def  calcular_predicao(sexo,temcancer,cancer_mama, idade_diagnostico,mutacaoGenetica,opc_bilateral,opc_ovario,tipo_molecular,historicoFMasculino,qtd_parent_2,parent_seg_grau,asc_judia):
    """ Esta função faz o calculo da predição com base nas respostas fornecidas pelo usuário e retora o resultado """

    valor_maximo_pesos = (1 + 5 + 2 + 4  + 5 + 5 + 2 + 3  + 3 + 4)
    
    print("Peso máximo: ",valor_maximo_pesos)

    valor_de_ponto = 0

    """ tem cancer de mama   """
    if temcancer == "SIM":
        valor_de_ponto += 1
    else:
        valor_de_ponto += 0
    
    """ historico pessoal de cancer de mamar bilateral"""
    if opc_bilateral == "SIM":
        valor_de_ponto += 5
    else:
        valor_de_ponto += 0

    """ teste genetico positivo """
    if  mutacaoGenetica =="SIM":
            valor_de_ponto  += 5
    else:
        valor_de_ponto
    
    if asc_judia == "SIM":
        valor_de_ponto   += 5
    else:
        valor_de_ponto

    if opc_ovario == "SIM":
        valor_de_ponto += 2
    else:
        valor_de_ponto += 0

    """ Histórico familiar de câncer de mama masculino da familia  """
    if historicoFMasculino == "SIM":
        valor_de_ponto += 2
    else:
        valor_de_ponto += 0
   
    """ Faixa de idade do diagnostico de câncer de mama:"""
    if idade_diagnostico == "Maior que 60 anos":
        valor_de_ponto  += 1
        
    elif idade_diagnostico == "Entre 55 e 60 anos":
        valor_de_ponto  += 1

    elif idade_diagnostico == "Entre 45 e 55 anos":
        valor_de_ponto  += 1

    elif idade_diagnostico == "Entre 35 e 44 anos":
        valor_de_ponto  += 1

    elif idade_diagnostico == "Entre 30 e 34 anos":
        valor_de_ponto  += 1

    elif idade_diagnostico == "Menor que 30 anos":
        valor_de_ponto  += 2
    else:
        valor_de_ponto += 0

           

    """ "Tipo molecular de câncer de mama: """
    if tipo_molecular == "Triplo Negativo":
        valor_de_ponto += 5 
    else:
       valor_de_ponto  += 0
    


    """ Quantidade parentes de primeiro grau com câncer de mama com idade < 50 anos: """
    if qtd_parent_2 == "um":
        valor_de_ponto += 1
    elif qtd_parent_2 == "Dois":
        valor_de_ponto += 2
    elif qtd_parent_2 == "Três":
        valor_de_ponto += 3
    else:
        valor_de_ponto += 0
    
    """ Quantidade de parentes de SEGUNDO grau com câncer de mama ou ovario com idade < 50 anos """
    if parent_seg_grau == "Um":
        valor_de_ponto += 1
    elif parent_seg_grau == "Dois":
        valor_de_ponto += 2
    elif parent_seg_grau == "Três":
        valor_de_ponto += 3
    else:
        valor_de_ponto += 0
    
    print("Valor parcial de pontos:", valor_de_ponto)


    
    print("valor maximo de pesos: ",valor_maximo_pesos)
    porcentagem = (valor_de_ponto/valor_maximo_pesos)*100
    porcentagem_arredondado = round(porcentagem, 2)
    return porcentagem_arredondado
    

    

    


