#Importação dos modulos utilizados como parametros de comparação
import initialInput, areaModule, tempModule, elecModule, math, operator, printList

#class protocol:
#    def __init__(self, name, alcance, snr, freq):
#        self.name = name
#        self.alcance = alcance
#        self.snr = snr
#        self.freq = freq

class myProtocol:
    
    def __init__(self, nome, alcance, snr, freq, rank):
        self.nome = nome
        self.alcance = alcance
        self.snr = snr
        self.freq = freq
        self.rank = rank

wifi2 = myProtocol("Wifi 2.4Ghz", 400, 4, 2400, 0)
wifi5 = myProtocol("Wifi 5Ghz", 200, 6, 5000, 0)
lora = myProtocol("LoRa", 5000, 15, 915, 0)
zigbee = myProtocol("ZigBee", 225, 9, 2400, 0)
bluetooth = myProtocol("Bluetooth", 40, 4, 2400, 0)
PLC = myProtocol("PLC", 100, 3, 30, 0)



def recconFreq(freq):
    if freq == 5:
        return 0
    elif freq == 30:
        return 1
    elif freq == 169:
        return 2
    elif freq == 433:
        return 3
    elif freq == 868:
        return 4
    elif freq == 915:
        return 5
    elif freq == 2400:
        return 6
    elif freq == 5000:
        return 7
    else:
        return -1
        
def ituModel(freq, dist):
    perda = (20*math.log10(freq)) - 28 + 30*math.log10(dist)
    return perda

def rankProtocol(protocol, frequencias, nBlocos):
    pontuacao = 0
    if(protocol.alcance < 10):
        pontuacao += nBlocos
    elif(protocol.alcance < 100):
        pontuacao += 2*nBlocos
    elif(protocol.alcance < 400):
        pontuacao +=3*nBlocos
    else:
        pontuacao +=4*nBlocos
    
    if(protocol.snr < 3):
        pontuacao += 1*nBlocos
    elif(protocol.snr < 6):
        pontuacao += 2*nBlocos
    elif(protocol.snr < 12):
        pontuacao += 3*nBlocos
    else:
        pontuacao += 4*nBlocos
    
    for x in range(0, nBlocos):
        if (int(frequencias[x][recconFreq(protocol.freq)]) >= 50 + protocol.snr):
            pontuacao += 0
        elif (int(frequencias[x][recconFreq(protocol.freq)]) >= 50):
            pontuacao += 1
        elif (int(frequencias[x][recconFreq(protocol.freq)]) >= 50 - protocol.snr):
            pontuacao += 2
        else:
            pontuacao += 3
            
    return pontuacao

def pontuacaoBase(alcance, snr):
    pontuacao = 0
    if(alcance < 10):
        pontuacao += 1
    elif(alcance < 100):
        pontuacao += 2
    elif(alcance < 400):
        pontuacao +=3
    else:
        pontuacao +=4
    
    if(snr < 3):
        pontuacao += 1
    elif(snr < 6):
        pontuacao += 2
    elif(snr < 12):
        pontuacao += 3
    else:
        pontuacao += 4

    return pontuacao

def rankBlock(pontuacaoBs, freq, frequencia):
    
    pontuacao = pontuacaoBs

    if int(frequencia[recconFreq(freq)]) >= 50 + snr:
        pontuacao += 0
    elif int(frequencia[recconFreq(freq)]) >= 50:
        pontuacao += 1
    elif int(frequencia[recconFreq(freq)]) >= 50 - snr:
        pontuacao += 2
    else:
        pontuacao += 3
            
    return pontuacao

def interferenceMap(frequencias, nBlocos, freq):
    interferences = []
    for x in range(0,nBlocos):
        interferences.append(frequencias[x][recconFreq(freq)])
    
    return interferences

def temperatureMap(temperatures, nBlocos):
    temperatura = []
    for x in range(0,nBlocos):
        temperatura.append(temperatures[x])
    
    return temperatura


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
    #print("\n" + nomeDoProjeto + "\n" + data)
    #print("A area total é de " + str(areaTotal) + "m² dividida em "+ str(nBlocos) + " blocos de " + str(areaPorBloco) + "m²")
    #print("As temperaturas dos blocos são:")
    #for x in range(0, nBlocos):
    #    print("Bloco " + str(x+1) + " -> " + str(temperatures[x] + "°C"))
    #print("As intesidades das frequências são: ")
    #print("Bloco   0-500Khz 2-30Mhz 169Mhz 433Mhz 868Mhz 915Mhz 2.4Ghz 5Ghz")
    #for x in range(0, nBlocos):
    #    print(" " + str(x+1) + "         " + str(frequencias[x][0]) + "      " + str(frequencias[x][1]) + "      " + str(frequencias[x][2]) + "     " + str(frequencias[x][3]) + "     " + str(frequencias[x][4]) + "     " + str(frequencias[x][5]) + "    " + str(frequencias[x][6]) + "    " + str(frequencias[x][7]))

    wifi2.rank = rankProtocol(wifi2, frequencias, nBlocos)
    lora.rank = rankProtocol(lora, frequencias, nBlocos)
    zigbee.rank = rankProtocol(zigbee, frequencias, nBlocos)
    PLC.rank = rankProtocol(PLC, frequencias, nBlocos)

    print("\n")
    protocoloEscolhido = []
    protocoloEscolhido.append(wifi2)
    protocoloEscolhido.append(zigbee)
    protocoloEscolhido.append(lora)
    protocoloEscolhido.append(PLC)
    protocoloEscolhido.sort(key=lambda x: x.rank, reverse = True)
    #print(protocoloEscolhido)
    for x in range(0, len(protocoloEscolhido)):
        print(str(x+1) + " - " + protocoloEscolhido[x].nome)

    order = 1
    while(order != 0):
        order = int(input("Qual meio de comunicação deseja escolher? (Ou 0 para sair)\n"))
        if(order != 0):
            mapaDeInterferencia = interferenceMap(frequencias, nBlocos, protocoloEscolhido[order-1].freq)
            mapaDeCalor = temperatureMap(temperatures, nBlocos)
            print("Mapa de interferencia:")
            printList.printList(mapaDeInterferencia)
            print("\nMapa de calor:")
            printList.printList(mapaDeCalor)
            print("\n")

    file = open("InterferenceMap.ppm", "w")
    
    #file = open("Results.txt","w")
    #file.write(nomeDoProjeto + "\n" + data + "\n")
    #file.write("A area total é de " + str(areaTotal) + "m² dividida em "+ str(nBlocos) + " blocos de " + str(areaPorBloco) + "m²\n")
    #file.write("As temperaturas dos blocos são:\n")
    #for x in range(0, nBlocos):
    #    file.write("Bloco " + str(x+1) + " -> " + str(temperatures[x] + "°C\n"))
    #file.write("As intesidades das frequências são: \n")
    #file.write("Bloco   0-500Khz 2-30Mhz 169Mhz 433Mhz 868Mhz 915Mhz 2.4Ghz 5Ghz\n")
    #for x in range(0, nBlocos):
    #    file.write(" " + str(x+1) + "         " + str(frequencias[x][0]) + "      " + str(frequencias[x][1]) + "      " + str(frequencias[x][2]) + "     " + str(frequencias[x][3]) + "     " + str(frequencias[x][4]) + "     " + str(frequencias[x][5]) + "    " + str(frequencias[x][6]) + "    " + str(frequencias[x][7] + "\n"))
    #file.close() 

    return

main()