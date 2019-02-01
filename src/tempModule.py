#Dados relacionados com temperatura
def tempParam(nBloc):
    #Vetor que guarda todas as temperaturas médias dos blocos
    temperatures = []
    for x in range(0 , nBloc):
        temporary = input("Coloque a temperatura do bloco " + str(x + 1) + ":")
        temperatures.append(temporary)
    return temperatures