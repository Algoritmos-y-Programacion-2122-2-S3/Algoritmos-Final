#Este selecciona compara con todos los siguientes e intercambia las posiciones con el menor que haya conseguido
def main():
    lista = [5, 7, 3, 1, 8, 4, 9, 2, 6]#1
    long = len(lista)#1

    for i in range(long - 1):#n
        menor = i#n
        for j in range(i+1, long):#n2
            if lista[menor] > lista[j]:#n2
                menor = j#n2
        temp = lista[i]#n
        lista[i] = lista[menor]#n
        lista[menor] = temp#n

    print(lista)#1 
    #2+5n+3n2 = O(n2)
        


main()