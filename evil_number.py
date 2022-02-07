def main():
    number_to_verify = int(input("Please give me a number to verify if is a evil number: \n"))
    number_list = transfor_to_binary(number_to_verify)
    is_even = is_ones_even_count(number_list)
    print_result(is_even, number_to_verify)

def print_result(is_even, number):
    if is_even:
        print("The number", number, "is a evil number")
    else:
        print("The number", number, "is not a evil number")

def is_ones_even_count(number_list):
    cont = 0
    for number in number_list:
        if number == 1:
            cont += 1
    
    return is_even(cont)

def is_even(cont):
    if cont % 2 == 0:
        return True
    else:
        return False

def transfor_to_binary(number_to_verify):
    number_list = []
    aux = number_to_verify

    while aux >= 2:
        number_list.append(aux % 2)
        if aux == 2 or aux == 3:
            number_list.append(aux // 2)
        aux //= 2
    number_list.reverse()
    print(number_list)
    return number_list

main()