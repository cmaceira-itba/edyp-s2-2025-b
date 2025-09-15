class Vendedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas = {}

    def agregar_venta(self, venta):
        if not self.ventas.get(venta.zona):
            self.ventas[venta.zona] = venta
            return

    def calcular_total(self):
        return sum(map(lambda x: x.cantidad, self.ventas.values()))

    def consultar_venta(self, zona):
        return self.ventas.get(zona, 0)
