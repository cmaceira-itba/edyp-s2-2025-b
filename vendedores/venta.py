class Venta:
    def __init__(self, zona, cantidad):
        self.zona = zona # Validar la zona
        self.cantidad = cantidad

    def __repr__(self):
        return str(self.cantidad)
