from quicksort import quicksort

def main():
    lista = [3, 5, 7, 1, 8, 4, 9, 2, 6]
    lista = quicksort(lista=lista)
    print(lista)
    value_to_find = 9
    print(binary_search(lista=lista, value_to_find=value_to_find))
    

def binary_search(lista, value_to_find):
    start = 0
    final = len(lista) - 1
    middle = (start + final) // 2
    if len(lista) == 1:
        if lista[0] == value_to_find:
            return lista[0]
        else:
            return -1
    if lista[middle] == value_to_find:
        return value_to_find
    elif value_to_find < lista[middle]:
        return binary_search(lista[start:middle], value_to_find)
    else:
        return binary_search(lista[middle+1:], value_to_find)
        
    
    



main()