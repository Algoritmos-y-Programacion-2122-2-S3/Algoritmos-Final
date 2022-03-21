class Producto:
    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

class Medicamento(Producto):
    def __init__(self, codigo, nombre, precio, existencia, componente):
        super().__init__(codigo, nombre, precio, existencia)
        self.componente = componente

class Alimentos(Producto):
    def __init__(self, codigo, nombre, precio, existencia,is_for_diabetic):
        super().__init__(codigo, nombre, precio, existencia)
        self.is_for_diabetic = is_for_diabetic

class Cosmeticos(Producto):
    def __init__(self, codigo, nombre, precio, existencia, f_vencimiento):
        super().__init__(codigo, nombre, precio, existencia)
        self.f_vencimiento = f_vencimiento

