
def main():
    lista = [3,5, 7, 1, 8, 4, 9, 2, 6]
    quicksort(lista)

def quicksort(lista):
    if len(lista) < 2:
        return lista
    menores, pivote, mayores = partition(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)

def partition(lista):
    menores = []
    mayores = []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        elif lista[i] > pivote:
            mayores.append(lista[i])
    return menores, pivote, mayores



main()