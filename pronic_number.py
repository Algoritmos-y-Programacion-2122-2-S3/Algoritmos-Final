def main():
    number_to_verify = int(input("Please give me a number to verify if is a pronic number: \n"))
    aux = number_to_verify - 1
    divider_list = get_dividers(number_to_verify)
    result_list = []
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
                result_list.append(divider_list[i])
                result_list.append(divider_list[j])
                break
        else:
            i += 1  

    if len(result_list) == 0:
        print("The number", number_to_verify, "is not a pronic number")
    else:
        print("The number", number_to_verify, "is a pronic number and the dividers are",result_list[0],result_list[1])
    

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