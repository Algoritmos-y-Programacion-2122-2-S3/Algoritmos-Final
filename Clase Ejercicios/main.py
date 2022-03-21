from cgi import print_form
from clientes import Cliente
from productos import Producto, Medicamento, Alimentos,Cosmeticos

def main():
    cont_clientes = 0
    producto1 = Medicamento("123","Atamel",10,1000,"Acetominofen")
    producto2 = Alimentos("456","Dorito",30,1000, False)
    producto3 = Cosmeticos("789","Valmy",20,1000,"10-10-2025")


    while cont_clientes < 100:
        cont_productos=0
        print("Bienvenido a la farmacia")
        print("Por favor ingresa la informacion solicitada")
        nombre = input("Por favor ingrese su nombre")
        apellido = input("Por favor ingrese su apellido")
        sexo = input("Por favor ingrese su sexo")
        direccion = input("Por favor ingrese su direccion")
        cedula = input("Por favor ingrese su cedula")
        telefono = input("Por favor ingrese su telefono")
        cliente = Cliente(nombre=nombre, apellido=apellido, sexo=sexo, direccion=direccion,cedula=cedula,telefono=telefono,total = 0)
        print("Indicanos que producto quieres")
        while cont_productos < 10:
            print("1.", producto1.nombre,"2.", producto2.nombre,"3.", producto3.nombre,"4. Orden completa")
            producto = input()
            if producto == "1":
                cliente.total += producto1.precio
            elif producto == "2":
                cliente.total += producto2.precio
            elif producto == "3":
                cliente.total += producto3.precio
            else:
                break
            cont_productos +=1
        print("******** FACTURA ********")
        print("Nombre:", cliente.nombre)
        print("Apellido:", cliente.apellido)
        print("Sexo:", cliente.sexo)
        print("Direccion:", cliente.direccion)
        print("Telefono:", cliente.telefono)
        print("Cedula:", cliente.cedula)
        print("Total:", cliente.total)

            
        cont_clientes += 1




main()