def main():
    num1 = 0
    num2 = 1
    cont = int(input("GIVE THE LIMIT"))
    result = 0

    while cont > 0: 
        print(num1, end=" ")
        result = num1 + num2
        num1 = num2
        num2 = result
        cont-=1
    




main()