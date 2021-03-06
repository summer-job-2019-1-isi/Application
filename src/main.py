#Importação dos modulos utilizados como parametros de comparação
import initialInput, areaModule, tempModule, elecModule, math, printList

#Classe comMiddle define uma classe para o meio de comunicação
#Os parametros passados se referem a:
# nome -> Nome do meio de comunicação
# alcance -> Alcance do meio de comunicação (sem-fio e cabeado)
# snr -> Refere-se ao SNR (Signal-to-Noise Rate) nos meios sem-fio, nos meios com fio é dividos em meios com tolerancia a ruidos (1) e meios
# com alta tolerância a ruídos (2)
# freq -> Frequencia de trabalho dos meios de comunicação sem-fio e é utilizado como taxa de transmissão nos meios cabeados
# tempMin -> Temperatura mínima suportada pelos meios cabeados
# tempMax -> Temperatura máxima suportada pelos meios cabeados
# rank -> Pontuação elencada pelas funções rankMiddle e rankCableMiddle
# cable -> Booleano indicando se o meio é cabeado ou não
class comMiddle:
    def __init__(self, nome, alcance, snr, freq, tempMin, tempMax, rank, cable, protocols):
        self.nome = nome
        self.alcance = alcance
        self.snr = snr
        self.freq = freq
        self.tempMin = tempMin
        self.tempMax = tempMax
        self.rank = rank
        self.cable = cable
        self.protocols = protocols


#Classe protocol define uma classe para cada protocolo
# name -> Nome do protocolo
# taxaMin -> Taxa de transmissão mínima dentro do range
# taxaMax -> Taxa de transmissão máxmia dentro do range
# rank -> Pontuação elencada pela função de rankProtocol
class protocol:
    def __init__(self, name, taxaMin, taxaMax, rank):
        self.name = name
        self.taxaMin = taxaMin
        self.taxaMax = taxaMax
        self.rank = rank

#Preenchimento de objetos

#Protocolos
profibusDP = protocol("Profibus DP", 10, 12000, 0)
profibusPA = protocol("Profibus PA", 32, 1000, 0)
profinet = protocol("Profinet", 10000, 100000, 0)
controlnet = protocol("Controlnet", 5000, 5000, 0)
interbus = protocol("Interbus", 500, 500, 0)
ethernet = protocol("Ethernet IP", 10000, 100000, 0)
modbus = protocol("Modbus TCP", 10000, 100000, 0)
canopen = protocol("Canopen", 10, 10000, 0)
ieee = protocol("IEEE 802.11", 2000, 10000, 0)
ieeea = protocol("IEEE 802.11a", 54000, 100000, 0)
ieeeb = protocol("IEEE 802.11b", 11000, 100000, 0)
ieeeg = protocol("IEEE 802.11g", 54000, 1000000, 0)
ieeeac = protocol("IEEE 802.11ac", 433000, 1000000, 0)
ieee154 = protocol("IEEE 802.15.4", 280, 1000, 0)
ieee151 = protocol("IEEE 802.15.1", 3000, 24000, 0)
lorawan = protocol("LoraWan", 50, 1000, 0)
ieee1901 = protocol("IEEE 1901", 2000, 20000, 0)

#Vetor de protocolos
protocolos = []
protocolos.append(profibusDP)
protocolos.append(profibusPA)
protocolos.append(profinet)
protocolos.append(controlnet)
protocolos.append(interbus)
protocolos.append(ethernet)
protocolos.append(modbus)
protocolos.append(canopen)
protocolos.append(ieee)
protocolos.append(ieeea)
protocolos.append(ieeeb)
protocolos.append(ieeeg)
protocolos.append(ieeeac)
protocolos.append(ieee154)
protocolos.append(ieee151)
protocolos.append(lorawan)
protocolos.append(ieee1901)


#Meios sem fio
wifi2 = comMiddle("Wifi 2.4Ghz", 400, 4, 2400, 0, 0, 0, False, [8,9,10,11])
wifi5 = comMiddle("Wifi 5Ghz", 200, 6, 5000, 0, 0, 0, False, [8,9,10,11,12])
lora = comMiddle("LoRa", 5000, 15, 915, 0, 0, 0, False, [15])
zigbee = comMiddle("ZigBee", 225, 9, 2400, 0, 0, 0, False, [13])
bluetooth = comMiddle("Bluetooth", 40, 4, 2400, 0, 0, 0, False, [14])
PLC = comMiddle("PLC", 100, 3, 30, 0, 0, 0, False, [16])

#Meios cabeados
caboCoaxialFi = comMiddle("Cabo Coaxial Diâmetro Fino", 185, 1, 10, -30, 60, 0, True, [0, 1, 2, 3, 4])
caboCoaxialGr = comMiddle("Cabo Coaxial Diâmetro Espesso", 500, 1, 10, -30, 80, 0, True, [0,1,2,3,4])
parTranc3 = comMiddle("Par Trançado Categoria 3", 100, 1, 10, -20, 60, 0, True, [0,1,2,5,6,7])
parTranc6 = comMiddle("Par Trançado Categoria 5 e 6", 100, 1, 1000, -20, 60, 0, True, [0,1,2,5,6,7])
fibraOpt125 = comMiddle("Fibra Óptica Tipo 62.5/125", 2000, 2, 1000, -20, 75, 0, True, [0,1,2,3,4])
fibraOptMono = comMiddle("Fira Óptica Monomodo", 550, 2, 1000, -20, 65, 0, True, [0,1,2,3,4])
fibraOptMult = comMiddle("Fibra Óptica Multimodo", 550, 2, 100000, -20, 75, 0, True, [0,1,2,3,4])

#Função de suporte que recebe uma intensidade de interferencia e retorna um vetor de 3 valores com a cor em RGB
def interferencToColor(freq):

    cor = []
    interference = int(freq)

    if(interference == -1):
        cor = [160, 160, 160]
    else:
        if(interference <= 50):
            cor.append(0)
        elif(interference >= 75):
            cor.append(255)
        else:
            cor.append(math.ceil((interference - 50) * (51/5)))

        if(interference >= 25 and interference <= 75):
            cor.append(255)
        elif(interference == 0 or interference == 100):
            cor.append(0)
        elif(interference < 25):
            cor.append(math.ceil((interference) * (51/5)))
        else:
            cor.append(math.ceil(255 - (interference - 75) * (51/5)))

        if(interference <= 25):
            cor.append(255)
        elif(interference >= 50):
            cor.append(0)
        else:
            cor.append(math.ceil(255 - (interference - 25) * (51/5)))
    
    return cor

    #cor = []
    #interference = int(freq)

#Função de suporte que recebe uma temperatura entre -30 e 150 e retorna um vetor de 3 valores com a cor em RGB
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

#Função de suporte para o vetor de frequencias, recebe a frequencia e retorna a posição no vetor
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

#Função que rankea meios de comunicação sem-fio, recebendo o objeto do meio de comunicação, o vetor de intensidade nas frequencias e o numero de blocos
#A pontuação começa em 0 e vai incrementando a partir de alguns parametros
#Alcance -> O alcance é incrementado a partir de um multiplicador que difere a partir do numero de blocos avaliados
#SNR -> Se altera da mesma forma que o alcance
#Interferencia -> A pontuação da interferencia é incrementada a partir de quantos dos blocos tem uma intensidade média
#maior ou menor que 50 +- o snr do meio, meios onde é visto menos interferencia dentro do seu espectro ganham uma maior pontuação
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
            pontuacao += 1
        elif (int(frequencias[x][recconFreq(protocol.freq)]) >= 50):
            pontuacao += 2
        elif (int(frequencias[x][recconFreq(protocol.freq)]) >= 50 - protocol.snr):
            pontuacao += 3
        else:
            pontuacao += 4
            
    return pontuacao

#Função que rankea meios de comunicação com fio, recebendo o objeto do meio de comunicação, o vetor de temperaturas e o numero de blocos
#Os parametros avaliados são
#Alcance -> Aumentam em fator do numero de blocos
#Tolerância a ruídos -> Concedem pontos para meios com tolerancia a ruidos (1) e mais pontos para meios com alta tolerância a ruídos (2)
#Taxa de transmissão -> Aumentam a pontuação a partir de um fator no numero de blocos
#Temperatura -> Concedem uma pontuação a partira da maior e/ou menor temperatura tolerada pelo meio de comunicação em relação a temperatura media do bloco
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

#Função que retorna um vetor com todas as interferencias de determinada frequencia
def interferenceMap(frequencias, nBlocos, freq):
    interferences = []
    for x in range(0,nBlocos):
        interferences.append(frequencias[x][recconFreq(freq)])
    
    return interferences

#Função que retorna um vetor com todas as temperaturas (Acho que essa função não faz nada)
def temperatureMap(temperatures, nBlocos):
    temperatura = []
    for x in range(0,nBlocos):
        temperatura.append(temperatures[x])
    
    return temperatura

#Função auxiliar que escreve em um arquivo 50 valores separados por um \n
def print50(value):
    for x in range(0, 50):
        file.write(str(value) + "\n")
    return

#Função de auxilio para imprimir protocolos
def printProtocols(protocols):
    for x in range (0, len(protocols)):
        print(str(x + 1) + " - " + str(protocols[x].name))
    return

#Função que dá pontos extras por protocolos que abranjam o a taxa necessaria
def extraPointsProtocol(meio, protocolos, taxaDeTrans, nBlocos):
    pontuacao = 0
    for x in range(0, len(meio.protocols)):
        if (int(taxaDeTrans) > protocolos[meio.protocols[x]].taxaMax):
            pontuacao += 0
        elif (int(taxaDeTrans) <= (protocolos[meio.protocols[x]].taxaMin - 1000)):
            pontuacao += 1*nBlocos
        else:
            pontuacao += math.ceil(2*nBlocos)
        
    pontuacao = math.ceil(pontuacao/len(meio.protocols))
    #print(str(meio.nome) + " - " + str(pontuacao))
    return pontuacao

#Função para rankear os protocolos
def rankProtocols(protocol, taxaDeTrans):
    pontuacao = 0
    if (int(taxaDeTrans) > protocol.taxaMax):
        pontuacao = 0
    elif (int(taxaDeTrans) <= protocol.taxaMin - 10000):
        pontuacao = 1
    elif (int(taxaDeTrans) <= protocol.taxaMin - 1000):
        pontuacao = 3
    else:
        pontuacao = 4
    return pontuacao


def main():
    #Dados iniciais do projeto
    nomeDoProjeto, data, taxaDeTrans = initialInput.projectData()
    #Dados relacionados a área
    areaTotal, nBlocos, areaPorBloco = areaModule.areaParam()
    #Dados relacionados a temperatura (temperature -> Array com temperaturas dos blocos)
    temperatures = tempModule.tempParam(int(nBlocos))
    #Dados relacionados a frequencia (frequencias -> Array de tuplas de frequencias p/ cada bloco)
    frequencias = elecModule.elecParam(int(nBlocos))

    


    #Aplicando a função de pontuação nos meios sem-fio escolhidos
    wifi2.rank = rankMiddle(wifi2, frequencias, nBlocos) + extraPointsProtocol(wifi2, protocolos, taxaDeTrans, nBlocos)
    wifi5.rank = rankMiddle(wifi5,frequencias, nBlocos) + extraPointsProtocol(wifi5, protocolos, taxaDeTrans, nBlocos)
    lora.rank = rankMiddle(lora, frequencias, nBlocos) + extraPointsProtocol(lora, protocolos, taxaDeTrans, nBlocos)
    zigbee.rank = rankMiddle(zigbee, frequencias, nBlocos) + extraPointsProtocol(zigbee, protocolos, taxaDeTrans, nBlocos)
    PLC.rank = rankMiddle(PLC, frequencias, nBlocos) + extraPointsProtocol(PLC, protocolos, taxaDeTrans, nBlocos)
    bluetooth.rank = rankMiddle(bluetooth, frequencias, nBlocos) + extraPointsProtocol(bluetooth, protocolos, taxaDeTrans, nBlocos)

    #Vetor com os meios sem fio
    nonCableMiddle = []
    nonCableMiddle.append(wifi2)
    nonCableMiddle.append(wifi5)
    nonCableMiddle.append(zigbee)
    nonCableMiddle.append(lora)
    nonCableMiddle.append(PLC)
    nonCableMiddle.append(bluetooth)
    #Ordenação dos meios por pontuação
    nonCableMiddle.sort(key=lambda x: x.rank, reverse = True)
    #Print de meios mais bem pontuados com seus respectivos numeros de ordem
    print("Melhores meios de comunicação sem-fio:")
    for x in range(0, len(nonCableMiddle)):
        print(str(x+1) + " - " + nonCableMiddle[x].nome + " - " + str(nonCableMiddle[x].rank))

    #Procedimento igual para meios cabeados
    #Meios cabeados são ordenados e organizados independentes dos meios não-cabeados
    caboCoaxialFi.rank = rankCableMiddle(caboCoaxialFi ,temperatures, nBlocos) + extraPointsProtocol(caboCoaxialFi, protocolos, taxaDeTrans, nBlocos)
    caboCoaxialGr.rank = rankCableMiddle(caboCoaxialGr ,temperatures, nBlocos) + extraPointsProtocol(caboCoaxialGr, protocolos, taxaDeTrans, nBlocos)
    parTranc3.rank = rankCableMiddle(parTranc3 ,temperatures, nBlocos) + extraPointsProtocol(parTranc3, protocolos, taxaDeTrans, nBlocos)
    parTranc6.rank = rankCableMiddle(parTranc6 ,temperatures, nBlocos) + extraPointsProtocol(parTranc6, protocolos, taxaDeTrans, nBlocos)
    fibraOpt125.rank = rankCableMiddle(fibraOpt125 ,temperatures, nBlocos) + extraPointsProtocol(fibraOpt125, protocolos, taxaDeTrans, nBlocos)
    fibraOptMono.rank = rankCableMiddle(fibraOptMono ,temperatures, nBlocos) + extraPointsProtocol(fibraOptMono, protocolos, taxaDeTrans, nBlocos)
    fibraOptMult.rank = rankCableMiddle(fibraOptMult ,temperatures, nBlocos) + extraPointsProtocol(fibraOptMult, protocolos, taxaDeTrans, nBlocos)

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
        print(str(x+len(nonCableMiddle)+1) + " - " + cableMiddle[x].nome + " - " + str(cableMiddle[x].rank))

    #Vetor com todos os meios disponiveis para que haja uma escolha do usuário
    #Os meios são apresentados em telas diferentes e apenas comparados entre si
    #O usuario tem a opção de escolher entre sem-fio e com fio, e é apresentado pra ele os melhores de cada um dos dois.
    allMiddle = []
    allMiddle.extend(nonCableMiddle)
    allMiddle.extend(cableMiddle)

    #Rankeamento dos protocolos a partir da taxa de transmissão
    profibusDP.rank = rankProtocols(profibusDP, taxaDeTrans)
    profibusPA.rank = rankProtocols(profibusPA, taxaDeTrans)
    profinet.rank = rankProtocols(profinet, taxaDeTrans)
    controlnet.rank = rankProtocols(controlnet, taxaDeTrans)
    interbus.rank = rankProtocols(interbus, taxaDeTrans)
    ethernet.rank = rankProtocols(ethernet, taxaDeTrans)
    modbus.rank = rankProtocols(modbus, taxaDeTrans)
    canopen.rank = rankProtocols(canopen, taxaDeTrans)
    ieee.rank = rankProtocols(ieee, taxaDeTrans)
    ieeea.rank = rankProtocols(ieeea, taxaDeTrans)
    ieeeb.rank = rankProtocols(ieeeb, taxaDeTrans)
    ieeeg.rank = rankProtocols(ieeeg, taxaDeTrans)
    ieeeac.rank = rankProtocols(ieeeac, taxaDeTrans)
    ieee151.rank = rankProtocols(ieee151, taxaDeTrans)
    ieee154.rank = rankProtocols(ieee154, taxaDeTrans)
    lorawan.rank = rankProtocols(lorawan, taxaDeTrans)
    ieee1901.rank = rankProtocols(ieee1901, taxaDeTrans)


    

        
    #Informações de seleção de meio de comunicação
    order = 1
    while(order != 0):
        order = int(input("Qual meio de comunicação deseja escolher? (Ou 0 para sair)\n"))
        if(order != 0):
            mapaDeInterferencia = interferenceMap(frequencias, nBlocos, allMiddle[order-1].freq)
            if(allMiddle[order-1].cable == False):
                print("Mapa de interferencia:")
                printList.printList(mapaDeInterferencia)
            print("\nMapa de calor:")
            printList.printList(temperatures)
            print("\n")
            
            #Organização e impressão de protocolos uteis
            choosenProtocols = []
            for x in range(0, len(allMiddle[order-1].protocols)):
                choosenProtocols.append(protocolos[allMiddle[order-1].protocols[x]])
            choosenProtocols.sort(key=lambda x: x.rank, reverse = True)

            print("Melhores protocolos para esse meio:")
            printProtocols(choosenProtocols)
            
            #Informações para imprimir o mapa de interferencia
            
            largura = int((math.sqrt(nBlocos)))
            if(int(math.ceil((nBlocos-(largura*largura))/largura)) > 0):
                altura = int(math.ceil((nBlocos-(largura*largura))/largura)) + largura
            else: 
                altura = largura
            nTotalDeBlocos = largura * altura
            nBlocosCinzas = nTotalDeBlocos - nBlocos
                
            #Informações para imprimir o mapa de calor
            vetorDeCor = []
            vetorDeCor.extend(temperatures)
            for x in range(0, nBlocosCinzas):
                vetorDeCor.append(-31)

            #Arquivo colorido do mapa de calor
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



            vetorDeInteferencia = []
            if(allMiddle[order-1].cable == False):
                for x in range(0, nBlocos):
                    vetorDeInteferencia.append(frequencias[x][recconFreq(allMiddle[order-1].freq)])
                for x in range(0, nBlocosCinzas):
                    vetorDeInteferencia.append(-1)
                
                #Informações para fazer a imagem colorida do mapa de interferência
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
            

        
    return

main()