def main():
    number_to_verify = int(input("Please give me a number to verify if is a hateful number: \n"))
    lista = []
    number_list = transfor_to_binary(number_to_verify, lista)
    number_list.reverse()
    print(number_list)
    ones_count = ones_counter(number_list)
    is_hateful_variable = is_hateful(ones_count)
    print_result(is_hateful_variable, number_to_verify)

def print_result(is_hateful, number):
    if is_hateful:
        print("The number", number, "is a hateful number")
    else:
        print("The number", number, "is not a hateful number")

def ones_counter(number_list):
    cont = 0
    for number in number_list:
        if number == 1:
            cont += 1
    
    return cont

def is_hateful(cont):
    if cont % 2 == 0:
        return False
    else:
        return True

def transfor_to_binary(number_to_verify, lista):
    aux = number_to_verify

    if aux >= 1:
        lista.append(aux % 2)
    else:
        return lista
    
    print(aux, lista)
    
    return transfor_to_binary(aux // 2, lista)
    
    

main()