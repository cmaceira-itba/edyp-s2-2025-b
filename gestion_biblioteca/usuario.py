class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_prestado(self,libro):
        self.libros_prestados.append(libro)

    def cantidad_prestados(self):
        return len(self.libros_prestados)

class UsuarioBasico(Usuario):
    prestamos_maximos = 1

    def __init__(self, nombre):
        super().__init__(nombre)

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= UsuarioBasico.prestamos_maximos:
            raise ValueError("No puedo solicitar mas libros")
        super().pedir_prestado(libro)

class UsuarioVip(Usuario):
    prestamos_maximos = 5

    def __init__(self, nombre):
        super().__init__(nombre)

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= UsuarioVip.prestamos_maximos:
            raise ValueError("No puedo solicitar mas libros")
        super().pedir_prestado(libro)
