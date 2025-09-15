class Empresa:
    def __init__(self):
        self.nombre = "Si se puede"
        self.vendedores = {}

    def agregar_vendedor(self, vendedor):
        if not self.vendedores.get(vendedor.nombre):
            self.vendedores[vendedor.nombre] = vendedor
            return
        raise ValueError("El vendedor ya existe")

    def calcular_ventas_totales(self):
        return sum(map(lambda x: x.calcular_total(), self.vendedores.values()))
