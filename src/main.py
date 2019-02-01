#Importação dos modulos utilizados como parametros de comparação
import initialInput, areaModule, tempModule, elecModule


def main():
    #Dados iniciais do projeto
    nomeDoProjeto, data = initialInput.projectData()
    #Dados relacionados a área
    areaTotal, nBlocos, areaPorBloco = areaModule.areaParam()
    #Dados relacionados a temperatura (temperature -> Array com temperaturas dos blocos)
    temperatures = tempModule.tempParam(int(nBlocos))
    #Dados relacionados a frequencia (frequencias -> Array de tuplas de frequencias p/ cada bloco)
    frequencias = elecModule.elecParam(int(nBlocos))
    #compareProtocols()
    #sortRankTable() -> pode ser substituido por um .sort() com tuplas de meio + pontuação
    #printResults()

    #Printing results
    print("\n" + nomeDoProjeto + "\n" + data)
    print("A area total é de " + str(areaTotal) + "m² dividida em "+ str(nBlocos) + " blocos de " + str(areaPorBloco) + "m²")
    print("As temperaturas dos blocos são:")
    for x in range(0, nBlocos):
        print("Bloco " + str(x+1) + " -> " + str(temperatures[x] + "°C"))
    print("As intesidades das frequências são: ")
    print("Bloco   0-500Khz 2-30Mhz 169Mhz 433Mhz 868Mhz 915Mhz 2.4Ghz 5Ghz")
    for x in range(0, nBlocos):
        print(" " + str(x+1) + "         " + str(frequencias[x][0]) + "      " + str(frequencias[x][1]) + "      " + str(frequencias[x][2]) + "     " + str(frequencias[x][3]) + "     " + str(frequencias[x][4]) + "     " + str(frequencias[x][5]) + "    " + str(frequencias[x][6]) + "    " + str(frequencias[x][7]))

    file = open("Results.txt","w")
    file.write(nomeDoProjeto + "\n" + data + "\n")
    file.write("A area total é de " + str(areaTotal) + "m² dividida em "+ str(nBlocos) + " blocos de " + str(areaPorBloco) + "m²\n")
    file.write("As temperaturas dos blocos são:\n")
    for x in range(0, nBlocos):
        file.write("Bloco " + str(x+1) + " -> " + str(temperatures[x] + "°C\n"))
    file.write("As intesidades das frequências são: \n")
    file.write("Bloco   0-500Khz 2-30Mhz 169Mhz 433Mhz 868Mhz 915Mhz 2.4Ghz 5Ghz\n")
    for x in range(0, nBlocos):
        file.write(" " + str(x+1) + "         " + str(frequencias[x][0]) + "      " + str(frequencias[x][1]) + "      " + str(frequencias[x][2]) + "     " + str(frequencias[x][3]) + "     " + str(frequencias[x][4]) + "     " + str(frequencias[x][5]) + "    " + str(frequencias[x][6]) + "    " + str(frequencias[x][7] + "\n"))
    file.close() 

    return




main()