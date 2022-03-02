def main():
    print("Welcome to calculator")
    limit = int(input("Enter how many numbers you want"))
    num1 = 0
    num2 = 1
    fibo_recursivo(num1,num2,limit)

def fibo_recursivo(num1,num2, limit):
    print(num1, end=" ")
    if limit == 0:
        return num2
    return fibo_recursivo(num2,num1+num2,limit -1)

main()