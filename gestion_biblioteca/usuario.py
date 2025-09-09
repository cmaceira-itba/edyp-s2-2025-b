class UsuarioError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class ExcededidoLimitePrestamosUsuarioError(UsuarioError):
    def __init__(self, usuario):
        super().__init__(f"Limite de prestamos excedido para {usuario}")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []


    def pedir_prestado(self,libro):
        raise NotImplemented()

    def cantidad_prestados(self):
        return len(self.libros_prestados)

class UsuarioBasico(Usuario):
    prestamos_maximos = 1

    def __init__(self, nombre):
        super().__init__(nombre)

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= UsuarioBasico.prestamos_maximos:
            raise ExcededidoLimitePrestamosUsuarioError(self)
        super().pedir_prestado(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}"

    def __repr__(self):
        return self.nombre

class UsuarioVip(Usuario):
    prestamos_maximos = 5

    def __init__(self, nombre):
        super().__init__(nombre)

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= UsuarioVip.prestamos_maximos:
            raise ValueError("No puedo solicitar mas libros")
        super().pedir_prestado(libro)
