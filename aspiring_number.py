def main():
    number_to_verify = int(input("Please give me a number to verify if is a pronic number: \n"))
    divider_list = get_dividers(number_to_verify)
    print("Divider List:",divider_list)

    new_number_to_verify = get_list_sum(divider_list)
    print("New number to verify:", new_number_to_verify)

    new_divider_list = get_dividers(new_number_to_verify)
    print("New Divider List:",new_divider_list)

    number_result_perfect = get_list_sum(new_divider_list)
    print("Result number:", number_result_perfect)

    if number_result_perfect == new_number_to_verify:
        print("The number:", number_to_verify, "is a aspiring number")
    else:
        print("The number:", number_to_verify, "is not a aspiring number")

def get_list_sum(the_list):
    result_number = 0
    for number in the_list:
        result_number += number
    return result_number


def get_dividers(number):
    aux = number - 1
    divider_list = []
    while aux > 0:
        if number % aux == 0:
            divider_list.append(aux)
        aux -= 1
    divider_list.reverse()
    return divider_list

main()