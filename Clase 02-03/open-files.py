def main():
    file = open("./archivo.txt")
    datos = file.read()
    file.close()
    print(datos.split("-"))


main()