#Este selecciona compara con todos los siguientes e intercambia las posiciones con el menor que haya conseguido
def main():
    lista = [5, 7, 3, 1, 8, 4, 9, 2, 6]
    long = len(lista)

    for i in range(long - 1):
        menor = i
        for j in range(i+1, long):
            if lista[menor] > lista[j]:
                menor = j
        temp = lista[i]
        lista[i] = lista[menor]
        lista[menor] = temp

    print(lista)
        


main()