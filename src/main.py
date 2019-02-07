#Importação dos modulos utilizados como parametros de comparação
import initialInput, areaModule, tempModule, elecModule, math, operator, printList

#class protocol:
#    def __init__(self, name, alcance, snr, freq):
#        self.name = name
#        self.alcance = alcance
#        self.snr = snr
#        self.freq = freq

class myProtocol:
    
    def __init__(self, nome, alcance, snr, freq, temp, rank, cable):
        self.nome = nome
        self.alcance = alcance
        self.snr = snr
        self.freq = freq
        self.temp = temp
        self.rank = rank
        self.cable = cable

wifi2 = myProtocol("Wifi 2.4Ghz", 400, 4, 2400, 0, 0, False)
wifi5 = myProtocol("Wifi 5Ghz", 200, 6, 5000, 0, 0, False)
lora = myProtocol("LoRa", 5000, 15, 915, 0, 0, False)
zigbee = myProtocol("ZigBee", 225, 9, 2400, 0, 0, False)
bluetooth = myProtocol("Bluetooth", 40, 4, 2400, 0, 0, False)
PLC = myProtocol("PLC", 100, 3, 30, 0, 0, False)




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
        
#def ituModel(freq, dist):
#    perda = (20*math.log10(freq)) - 28 + 30*math.log10(dist)
#    return perda

def rankMiddle(protocol, frequencias, nBlocos):
    pontuacao = 0
    if(protocol.alcance < 10):
        pontuacao += nBlocos
    elif(protocol.alcance < 100):
        pontuacao += 2*nBlocos
    elif(protocol.alcance < 400):
        pontuacao +=3*nBlocos
    else:
        pontuacao +=4*nBlocos

    if(protocol.cable == False):
        if(protocol.snr < 3):
            pontuacao += 1*nBlocos
        elif(protocol.snr < 6):
            pontuacao += 2*nBlocos
        elif(protocol.snr < 12):
            pontuacao += 3*nBlocos
        else:
            pontuacao += 4*nBlocos
    
    #if(protocol.cable == True)


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

def print50(value):
    for x in range(0, 50):
        file.write(str(value) + "\n")
    return


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

    wifi2.rank = rankMiddle(wifi2, frequencias, nBlocos)
    lora.rank = rankMiddle(lora, frequencias, nBlocos)
    zigbee.rank = rankMiddle(zigbee, frequencias, nBlocos)
    PLC.rank = rankMiddle(PLC, frequencias, nBlocos)

    print("\n")
    nonCableMiddle = []
    nonCableMiddle.append(wifi2)
    nonCableMiddle.append(wifi5)
    nonCableMiddle.append(zigbee)
    nonCableMiddle.append(lora)
    nonCableMiddle.append(PLC)
    nonCableMiddle.sort(key=lambda x: x.rank, reverse = True)
    #print(nonCableMiddle)
    for x in range(0, len(nonCableMiddle)):
        print(str(x+1) + " - " + nonCableMiddle[x].nome)

    #cableMiddle = []

    

    order = 1
    while(order != 0):
        order = int(input("Qual meio de comunicação deseja escolher? (Ou 0 para sair)\n"))
        if(order != 0):
            mapaDeInterferencia = interferenceMap(frequencias, nBlocos, nonCableMiddle[order-1].freq)
            mapaDeCalor = temperatureMap(temperatures, nBlocos)
            print("Mapa de interferencia:")
            printList.printList(mapaDeInterferencia)
            print("\nMapa de calor:")
            printList.printList(mapaDeCalor)
            print("\n")

    


    largura = int(math.sqrt(nBlocos))
    if(int(math.ceil((nBlocos-(largura*largura))/largura)) > 0):
        altura = int(math.ceil((nBlocos-(largura*largura))/largura))
    else: 
        altura = largura
    nTotalDeBlocos = largura * altura
    nBlocosCinzas = nTotalDeBlocos - nBlocos

    vetorDeCor = []
    vetorDeCor.extend(temperatures)
    for x in range(0, nBlocosCinzas):
        vetorDeCor.append(0)

    print(vetorDeCor)

    file = open("InterferenceMap.ppm", "w")
    file.write("P3\n")
    file.write(str(50*largura) + " " + str(50*altura) + "\n")

    print("largura é: "+ str(largura))
        
    cor = 0
    for y in range(0, 50):
        for x in range(0, (largura*50)):
            if(x != 0 and x%50 == 0):
                cor += 1
                file.write(str(vetorDeCor[cor]) + "\n")
            else:
                file.write(str(vetorDeCor[cor]) + "\n")    
        cor -= largura -1
        
    #file.write()
    # largura sqrt = int(math.sqrt(nBlocos))
    # altura sqrt + int((nBlocos%sqrt)) 
    
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