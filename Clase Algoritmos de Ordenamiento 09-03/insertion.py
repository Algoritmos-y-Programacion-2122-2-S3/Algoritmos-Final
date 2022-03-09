
def main():
    lista = [3,5, 7, 1, 8, 4, 9, 2, 6]
    long = len(lista)

    for i in range(long): # 2
        valor = lista[i] #3
        temp = i # 2
        j = i-1 # 1
        while j >= 0 and valor < lista[j]:
            lista[temp] = lista[j]
            lista[j] =  valor
            j -= 1
            temp -=1

    print(lista)
        


main()