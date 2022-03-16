
def main():
    lista = [3,5, 7, 1, 8, 4, 9, 2, 6] #1
    long = len(lista) # 1

    for i in range(long): # n
        valor = lista[i] # n
        temp = i #  n
        j = i-1 # n
        while j >= 0 and valor < lista[j]: # n2
            lista[temp] = lista[j]# n2
            lista[j] =  valor#n2
            j -= 1#n2
            temp -=1#n2

    print(lista)#1
        # 3 + 4n + 5n2 =  peor escenario O(n2) - mejor escenario O(n)


main()