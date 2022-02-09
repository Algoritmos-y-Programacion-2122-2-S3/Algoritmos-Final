
def main():
    num1 = 0
    num2 = 1
    limit = 20
    number_to_verify = int(input("Give me a number to verify: \n"))
    result = 0
    fibo_list = []
    position = - 1

    while limit > 0: 
        fibo_list.append(num1)
        result = num1 + num2
        num1 = num2
        num2 = result
        limit -= 1

    print("La serie de fibonacci es:", fibo_list)

    if fibo_list.count(number_to_verify) == 0:
        print("The number",number_to_verify,"is not in the fibonacci serie")
    else:
        position = fibo_list.index(number_to_verify)
        print("The number",number_to_verify,"is in the fibonacci serie in the position:", position )

    if position > - 1:
        position_base_eight = transfor_to_base_eight(position)
        position_string = ""
        for digit in position_base_eight:
            position_string += str(digit)
        print("La posicion en base 8 es:",position_string )

    else:
        print("Tarea calcular si es numero primo")
        print("***END***")    

def transfor_to_base_eight(number_to_verify):
    number_list = []
    aux = number_to_verify

    while aux >= 1:
        print(aux) 
        number_list.append(aux % 8)
        aux //= 8
    number_list.reverse()
    print(number_list)
    return number_list
    

main()