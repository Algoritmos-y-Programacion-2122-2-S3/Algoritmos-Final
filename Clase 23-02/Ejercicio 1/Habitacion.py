class Habitacion:
    __atributo = "AAAA"
    def __init__(self, number):
        self.banos = number

    def get_atributo(self):
        return self.__atributo
    
    def limpiar_habitacion(self):
        print("Se limpio la habitacion")

class Sala(Habitacion):
    def __init__(self, number):
        self.numero = number

class Comedor(Habitacion):
    def __init__(self, number):
        self.numero = number