from turtle import pos


def main():
    number_to_verify = int(input("Please give me a number to verify if is a pronic number: \n"))
    aux = number_to_verify - 1
    divider_list = get_dividers(number_to_verify)
    print("Divider",divider_list)
    i = 0
    j = 0
    while i < len(divider_list):
        if i + 1 < len(divider_list):
            j = i + 1
        else:
            break
        if divider_list[i] * divider_list[j] == number_to_verify:
            if divider_list[j] == divider_list[i] + 1:
                print("TRUE")
                break
        else:
            i += 1  

    print("Fracaso")
    

    
    

def get_dividers(number):
    aux = number - 1
    divider_list = []
    while aux > 1:
        if number % aux == 0:
            divider_list.append(aux)
        aux -= 1
    divider_list.reverse()
    return divider_list




main()