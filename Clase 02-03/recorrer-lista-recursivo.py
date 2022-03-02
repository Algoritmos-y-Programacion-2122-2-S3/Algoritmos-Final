def main():
    print("Welcome to list search")
    int_list = [0,1,2,3,4,5,6,7,8,9]
    number = int(input("What number: "))
    position = 0
    result = search(int_list,number,position)
    if result == -1:
        print("The number",number,"was not found")
    else:
        print("The number",number,"was found")

def search(int_list,number,position):
    if position == len(int_list) - 1:
        if int_list[position] == number:
            return number
        else:
            return -1
    else:
        if int_list[position] == number:
            return number
    return search(int_list,number,position+1)

main()