from libro import Libro
from usuario import Usuario

class BibliotecaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class UsuarioRepetidoError(BibliotecaError):
    def __init__(self):
        super().__init__("Usuario ya existe en la biblioteca")

class LibroRepetidoError(BibliotecaError):
    def __init__(self):
        super().__init__("Libro ya existe en la biblioteca")

class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def get_nombre(self):
        return self.nombre

    def get_libros(self):
        return self.libros

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("No es un Libro")
        if libro in self.libros:
            return
        self.libros.append(libro)

    def cantidad_libros(self):
        return len(self.libros)

    def get_usuarios(self):
        return self.usuarios

    def agregar_usuario(self, usuario):
        # Valido que el usuario no se encuentre ya en la bibloteca
        if not isinstance(usuario, Usuario):
            raise TypeError("No es un Usuario")
        if usuario in self.usuarios:
            raise UsuarioRepetidoError()
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        # No puedo prestar un libro a un usuario que no pertenece a la bibl
        if usuario not in self.usuarios:
            return
        # No puedo prestar un libro que no pertenece a la bibloteca
        if libro not in self.libros:
            return

        self.libros.remove(libro)
        usuario.pedir_prestado(libro)

    def cantidad_prestados(self):
        prestados = 0
        for usuario in self.usuarios:
            prestados += usuario.cantidad_prestados()
        return prestados
