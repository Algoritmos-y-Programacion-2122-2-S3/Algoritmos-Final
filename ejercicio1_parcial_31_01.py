from tracemalloc import start


def main():
    number_to_verify = input("Please give a number:\n")

    if number_to_verify.isnumeric:
        prime_list = []
        divider_list = []
        result_list = []
        number_to_verify = int(number_to_verify)
        aux = number_to_verify - 1
        is_prime = True

        if number_to_verify == 1:
            is_prime = False
        else:
            while aux > 1:
                if number_to_verify % aux == 0:
                    divider_list.append(aux)
                aux -= 1
        print("Divider",divider_list)

        for number_divider in divider_list:
            if number_divider == 2: 
                 prime_list.append(number_divider)
            else:
                aux2 = number_divider - 1
                while aux2 > 1:
                    if number_divider % aux2 == 0:
                        is_prime = False
                    aux2 -=1
                    if aux2 == 1:
                        if is_prime:
                            prime_list.append(number_divider)
                        is_prime = True

        cont=0
        cont2= 1
        print("Primos",prime_list)
        while cont < len(prime_list):
            cont2= cont + 1
            if len(result_list) > 0:
                print("The two prime numbers are:", result_list)
                break
            while cont2 < len(prime_list):
                result = prime_list[cont] * prime_list[cont2]
                if result == number_to_verify:
                    result_list.append(prime_list[cont])
                    result_list.append(prime_list[cont2])
                    break
                cont2 += 1
            cont += 1

        if len(result_list) == 0:
            print("There are not prime numbers")


    else: 
        print("This is not valid")





main()