#Importação dos modulos utilizados como parametros de comparação
import initialInput, areaModule, tempModule, elecModule, math, operator, printList

#class protocol:
#    def __init__(self, name, alcance, snr, freq):
#        self.name = name
#        self.alcance = alcance
#        self.snr = snr
#        self.freq = freq

class myProtocol:
    
    def __init__(self, nome, alcance, snr, freq, tempMin, tempMax, rank, cable):
        self.nome = nome
        self.alcance = alcance
        self.snr = snr
        self.freq = freq
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.rank = rank
        self.cable = cable

wifi2 = myProtocol("Wifi 2.4Ghz", 400, 4, 2400, 0, 0, 0, False)
wifi5 = myProtocol("Wifi 5Ghz", 200, 6, 5000, 0, 0, 0, False)
lora = myProtocol("LoRa", 5000, 15, 915, 0, 0, 0, False)
zigbee = myProtocol("ZigBee", 225, 9, 2400, 0, 0, 0, False)
bluetooth = myProtocol("Bluetooth", 40, 4, 2400, 0, 0, 0, False)
PLC = myProtocol("PLC", 100, 3, 30, 0, 0, 0, False)


caboCoaxialFi = myProtocol("Cabo Coaxial Diâmetro Fino", 185, 1, 10, -30, 60, 0, True)
caboCoaxialGr = myProtocol("Cabo Coaxial Diâmetro Espesso", 500, 1, 10, -30, 80, 0, True)
parTranc3 = myProtocol("Par Trançado Categoria 3", 100, 1, 10, -20, 60, 0, True)
parTranc6 = myProtocol("Par Trançado Categoria 5 e 6", 100, 1, 1000, -20, 60, 0, True)
fibraOpt125 = myProtocol("Fibra Óptica Tipo 62.5/125", 2000, 2, 1000, -20, 75, 0, True)
fibraOptMono = myProtocol("Fira Óptica Monomodo", 550, 2, 1000, -20, 65, 0, True)
fibraOptMult = myProtocol("Fibra Óptica Multimodo", 550, 2, 100000, -20, 75, 0, True)


def interferencToColor(freq):
    cor = []
    interference = int(freq)

    if(interference == -1):
        cor = [160, 160, 160]
    else:
        if(interference >= 0 and interference <= 25):
            cor = [255,math.ceil(interference*12.75),0]
        elif(interference > 25 and interference <= 50):
            cor = [(255 - math.ceil((interference-25)*(12.75))),255,0]
        elif(interference > 50 and interference <= 75):
            cor = [0,255,math.ceil((interference-50)*12.75)]
        else:
            cor = [0,(255 - math.ceil((interference-75)*(12.75))),255]
    
    return cor

def temperatureToColor(temperature):
    cor = []
    temperature = int(temperature) + 30

    if(temperature == -1):
        cor = [160, 160, 160]
    else:
        if(temperature <= 90):
            cor.append(0)
        elif(temperature >= 135):
            cor.append(255)
        else:
            cor.append(math.ceil((temperature - 90) * (17/3)))

        if(temperature >= 45 and temperature <= 135):
            cor.append(255)
        elif(temperature == 0 or temperature == 180):
            cor.append(0)
        elif(temperature < 45):
            cor.append(math.ceil((temperature) * (17/3)))
        else:
            cor.append(math.ceil(255 - (temperature - 135) * (17/3)))

        if(temperature <= 45):
            cor.append(255)
        elif(temperature >= 90):
            cor.append(0)
        else:
            cor.append(math.ceil(255 - (temperature - 45) * (17/3)))
    
    return cor

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

def rankCableMiddle(protocol, temperatures, nBlocos):

    pontuacao = 0
    if(protocol.alcance <= 100):
        pontuacao += nBlocos
    elif(protocol.alcance <= 200):
        pontuacao += 2*nBlocos
    elif(protocol.alcance <= 600):
        pontuacao +=3*nBlocos
    else:
        pontuacao +=4*nBlocos

    if(protocol.snr == 1):
        pontuacao += nBlocos
    elif(protocol.snr == 2):
        pontuacao += 4*nBlocos

    if(protocol.freq <= 10):
        pontuacao += 0
    elif(protocol.freq <= 100):
        pontuacao += math.ceil(0.5*nBlocos)
    elif(protocol.freq <= 1000):
        pontuacao += nBlocos
    else:
        pontuacao += 2*nBlocos

    for x in range(0, nBlocos):
        if (int(temperatures[x]) >= protocol.tempMax or int(temperatures[x]) <= protocol.tempMin):
            pontuacao += 0
        elif (int(temperatures[x]) >= (protocol.tempMax - 10) or int(temperatures[x]) <= (protocol.tempMin + 10)):
            pontuacao += 1
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

    #Meios não cabeados escolhidos
    wifi2.rank = rankMiddle(wifi2, frequencias, nBlocos)
    wifi5.rank = rankMiddle(wifi5,frequencias, nBlocos)
    lora.rank = rankMiddle(lora, frequencias, nBlocos)
    zigbee.rank = rankMiddle(zigbee, frequencias, nBlocos)
    PLC.rank = rankMiddle(PLC, frequencias, nBlocos)
    bluetooth.rank = rankMiddle(bluetooth, frequencias, nBlocos)

    print("\n")
    nonCableMiddle = []
    nonCableMiddle.append(wifi2)
    nonCableMiddle.append(wifi5)
    nonCableMiddle.append(zigbee)
    nonCableMiddle.append(lora)
    nonCableMiddle.append(PLC)
    nonCableMiddle.append(bluetooth)
    nonCableMiddle.sort(key=lambda x: x.rank, reverse = True)
    print("Melhores meios de comunicação sem-fio:")
    for x in range(0, len(nonCableMiddle)):
        print(str(x+1) + " - " + nonCableMiddle[x].nome)

    caboCoaxialFi.rank = rankCableMiddle(caboCoaxialFi ,temperatures, nBlocos)
    caboCoaxialGr.rank = rankCableMiddle(caboCoaxialGr ,temperatures, nBlocos)
    parTranc3.rank = rankCableMiddle(parTranc3 ,temperatures, nBlocos)
    parTranc6.rank = rankCableMiddle(parTranc6 ,temperatures, nBlocos)
    fibraOpt125.rank = rankCableMiddle(fibraOpt125 ,temperatures, nBlocos)
    fibraOptMono.rank = rankCableMiddle(fibraOptMono ,temperatures, nBlocos)
    fibraOptMult.rank = rankCableMiddle(fibraOptMult ,temperatures, nBlocos)

    cableMiddle = []
    cableMiddle.append(parTranc3)
    cableMiddle.append(parTranc6)
    cableMiddle.append(caboCoaxialFi)
    cableMiddle.append(caboCoaxialGr)
    cableMiddle.append(fibraOpt125)
    cableMiddle.append(fibraOptMono)
    cableMiddle.append(fibraOptMult)
    cableMiddle.sort(key=lambda x: x.rank, reverse = True)
    print("\n")
    print("Melhores meios de comunicação com fio:")
    for x in range(0, len(cableMiddle)):
        print(str(x+len(nonCableMiddle)+1) + " - " + cableMiddle[x].nome)

    allMiddle = []
    allMiddle.extend(nonCableMiddle)
    allMiddle.extend(cableMiddle)



   
    
    #Informações de seleção de meio de comunicação
    order = 1
    while(order != 0):
        order = int(input("Qual meio de comunicação deseja escolher? (Ou 0 para sair)\n"))
        if(order != 0):
            mapaDeInterferencia = interferenceMap(frequencias, nBlocos, allMiddle[order-1].freq)
            mapaDeCalor = temperatureMap(temperatures, nBlocos)
            if(allMiddle[order-1].cable == False):
                print("Mapa de interferencia:")
                printList.printList(mapaDeInterferencia)
            print("\nMapa de calor:")
            printList.printList(mapaDeCalor)
            print("\n")
            
            #Informações para imprimir o mapa de interferencia
            if(allMiddle[order-1].cable == False):
                largura = int(math.ceil(math.sqrt(nBlocos)))
                if(int(math.ceil((nBlocos-(largura*largura))/largura)) > 0):
                    altura = int(math.ceil((nBlocos-(largura*largura))/largura))
                else: 
                    altura = largura
                nTotalDeBlocos = largura * altura
                nBlocosCinzas = nTotalDeBlocos - nBlocos
                vetorDeInteferencia = []
                for x in range(0, nBlocos):
                    vetorDeInteferencia.append(frequencias[x][recconFreq(allMiddle[order-1].freq)])
                for x in range(0, nBlocosCinzas):
                    vetorDeInteferencia.append(-1)
                
                file = open("InterferenceMap.ppm", "w")
                file.write("P3\n")
                file.write(str(50*largura) + " " + str(50*altura) + "\n")
                file.write("255\n")
                    
                cor = 0
                for z in range(0, altura):
                    for y in range(0, 50):
                        for x in range(0, (largura*50)):
                            if(x != 0 and x%50 == 0):
                                cor += 1
                                numeroCor = interferencToColor(vetorDeInteferencia[cor])
                                file.write(str(numeroCor[0]) + " " + str(numeroCor[1]) + " "+ str(numeroCor[2]) + "\n")
                            else:
                                numeroCor = interferencToColor(vetorDeInteferencia[cor])
                                file.write(str(numeroCor[0]) + " " + str(numeroCor[1]) + " "+ str(numeroCor[2]) + "\n")
                        cor -= largura -1
                    cor += largura
            

        
    #Informações para imprimir o mapa de calor
    vetorDeCor = []
    vetorDeCor.extend(temperatures)
    for x in range(0, nBlocosCinzas):
        vetorDeCor.append(-31)

    #Imprimindo mapa de calor
    file = open("HeatMap.ppm", "w")
    file.write("P3\n")
    file.write(str(50*largura) + " " + str(50*altura) + "\n")
    file.write("255\n")
    cor = 0
    for z in range(0, altura):
        for y in range(0, 50):
            for x in range(0, (largura*50)):
                if(x != 0 and x%50 == 0):
                    cor += 1
                    numeroCor = temperatureToColor(vetorDeCor[cor])
                    file.write(str(numeroCor[0]) + " " + str(numeroCor[1]) + " "+ str(numeroCor[2]) + "\n")
                else:
                    numeroCor = temperatureToColor(vetorDeCor[cor])
                    file.write(str(numeroCor[0]) + " " + str(numeroCor[1]) + " "+ str(numeroCor[2]) + "\n")
            cor -= largura -1
        cor += largura
        
    return

main()