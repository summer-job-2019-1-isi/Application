def elecParam(nBloc):
    frequencias = []
    for x in range(0,nBloc):
        freq1 = input("Intensidade média na frequência 0-500Khz (em db) do bloco " + str(x+1)+": ")
        freq2 = input("Intensidade média na frequência 2-30Mhz (em db) do bloco " + str(x+1)+": ")
        freq3 = input("Intensidade na frequência 169Mhz (em db) do bloco " + str(x+1)+": ")
        freq4 = input("Intensidade na frequência 433Mhz (em db) do bloco " + str(x+1)+": ")
        freq5 = input("Intensidade na frequência 868Mhz (em db) do bloco " + str(x+1)+": ")
        freq6 = input("Intensidade na frequência 915Mhz (em db) do bloco " + str(x+1)+": ")
        freq7 = input("Intensidade na frequência 2.4Ghz (em db) do bloco " + str(x+1)+":")
        freq8 = input("Intensidade na frequência 5Ghz (em db) do bloco " + str(x+1)+": ")
        frequencias.append((freq1, freq2, freq3, freq4, freq5, freq6, freq7, freq8))
    return frequencias


#   Bloco   0-500Khz 2-30Mhz 169Mhz 433Mhz 868Mhz 915Mhz 2.4Ghz 5Ghz
#     1     freq1    freq2   freq3  freq4  freq5  freq6  freq7  freq8
#     2
#     3