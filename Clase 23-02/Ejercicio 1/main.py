from Habitacion import Habitacion
from Habitacion import Comedor
from Habitacion import Sala

def main():
    habitacion = Habitacion(12)
    habitacion.limpiar_habitacion()
    comedor = Comedor(12)
    sala = Sala(12)
    sala.limpiar_habitacion()
    print(habitacion.get_atributo())
    print("Hab-Comedor", isinstance(comedor, Habitacion))
    print("Comedor-Comedor", isinstance(comedor, Comedor))
    print("Sala-Comedor", isinstance(sala, Comedor))
    print("Sala-Habi", isinstance(sala, Habitacion))
    print("Sala-Sala",isinstance(sala, Sala))

main()