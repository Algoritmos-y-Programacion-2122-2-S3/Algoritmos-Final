def main():
    lista = [3, 5, 7, 1, 8, 4, 9, 2, 6]
    value_to_find = 10
    print(lineal_search(lista, value_to_find))

def lineal_search(lista, value_to_find):
    for number in lista:
        if number == value_to_find:
            return value_to_find
    return -1

main()