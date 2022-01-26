def main():
    rows_number = int(input("How many rows you want?\n"))
    row_conter = 1
    current_row = 0

    while current_row < rows_number:
        if current_row == 0:
            print(row_conter)
        else:
            aux = row_conter
            while aux >= 1:
                if aux == 1:
                    print(aux)
                else:
                    print(aux, end= " ")
                aux -= 2
        current_row +=1
        row_conter += 2


if __name__ == "__main__":
    main()