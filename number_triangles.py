def main():
    rows_number = int(input("How many rows you want?\n"))
    rowConter = 1
    currentRow = 0

    while currentRow < rows_number:
        if currentRow == 0:
            print(rowConter)
        else:
            aux = rowConter
            while aux >= 1:
                if aux == 1:
                    print(aux)
                else:
                    print(aux, end= " ")
                aux -= 2
        currentRow +=1
        rowConter += 2


if __name__ == "__main__":
    main()