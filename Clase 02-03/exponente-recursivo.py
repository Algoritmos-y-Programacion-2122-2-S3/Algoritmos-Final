def main():
    print("Welcome to calculator")
    base = int(input("Give me the base number"))
    exp = int(input("Give me the exp number"))
    print ("The result is: ",exponential(exp= exp,base= base))

    hola = "5-5-5-4"
    print(hola.split("-"))

def exponential(base,exp):
    if exp == 1:
        return base
    return base * exponential(base,exp-1)

main()