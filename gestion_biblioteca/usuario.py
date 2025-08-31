class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_prestado(self,libro):
        self.libros_prestados.append(libro)

    def cantidad_prestados(self):
        return len(self.libros_prestados)
