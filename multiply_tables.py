def main():
    table = int(input("What table do you want to see: \n"))

    for i in range(1,11):
        print(table,str(i) + f" = {table * i}", sep=" x ")
        


if __name__ == "__main__":
    main()