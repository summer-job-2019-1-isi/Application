#Dados relacionados a area
def areaParam():
    areaTotal = int(input("Insira a área total em m²: "))
    #O numero de blocos que o usuario deseja dividir a planta
    nBlocos = int(input("Selecione o numero de blocos que deseja dividir a área \n(Quanto mais blocos, mais preciso o resultado será, porém será necessário mais medições) \n 1 - 2 - 4 - 6 - 8 - 10: "))
    areaPorBloco = areaTotal / nBlocos
    #O tamanho dos blocos é arrendodado com 2 casa decimais
    areaPorBloco = round(areaPorBloco, 2)
    return areaTotal, nBlocos, areaPorBloco

