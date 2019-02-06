import math

def printList(list):
    sqrt = int(math.sqrt(len(list)))

    for x in range(0, len(list)):

        print(' ' + str(list[x]) + ' | ', end = '')

        if(int(x+1) % int(sqrt) == 0 and int(x) > 0):
            print()
            for y in range(0, sqrt):
                print('-----', end = '')
            print()
    return 