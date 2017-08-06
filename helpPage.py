def getHelp(function):
    if(function == 'conv'):
        answer = "Uso da funcao: \n"+"numero_da funcao opcao_de_numero numero base_de destino\n"+ "Ex: conv dec 15 2"
    elif(function == 'clima'):
        answer = "Retorna o as estatisticas climaticas na cidade escolhida.\n Uso da funcao:\nclima cidade_escolhida\nEx: clima Brasilia"
    elif(function == 'hora'):
    	answer = "Retorna a hora na cidade escolhida.\nUso da funcao:\nhora cidade_escolhida\nEx: hora Brasilia"
    return answer
