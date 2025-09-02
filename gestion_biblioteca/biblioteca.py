from libro import Libro
from usuario import Usuario, UsuarioError

class BibliotecaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class UsuarioRepetidoError(BibliotecaError):
    def __init__(self):
        super().__init__("Usuario ya existe en la biblioteca")

class UsuarioNoPerteneceError(BibliotecaError):
    def __init__(self):
        super().__init__("Usuario no pertenece a la biblioteca")

class LibroRepetidoError(BibliotecaError):
    def __init__(self):
        super().__init__("Libro ya existe en la biblioteca")

class LibroNoPerteneceError(BibliotecaError):
    def __init__(self):
        super().__init__("Libro no pertenece a la biblioteca")

class PrestamoImposibleError(BibliotecaError):
    def __init__(self):
        super().__init__("El prestamo no es posible")

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
            raise LibroRepetidoError()
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

    def retirar_libro(self, libro):
        self.libros.remove(libro)
        return libro

    def validar_usuario_socio(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("No es un Usuario")
        # No puedo prestar un libro a un usuario que no pertenece a la bibl
        if usuario not in self.usuarios:
            raise UsuarioNoPerteneceError()

    def validar_libro(self, libro):
        if not isinstance(libro, Usuario):
            raise TypeError("No es un Libro")
        # No puedo prestar un libro a un usuario que no pertenece a la bibl
        if libro not in self.libros:
            raise LibroNoPerteneceError()

    def prestar_libro(self, usuario, libro):
        try:
            self.validar_usuario_socio(usuario)
            self.validar_libro(libro)
            # Retiro el libro de la biblioteca y se lo entrego al usuario
            # Por que lo hacemos en una sola linea?
            usuario.pedir_prestado(self.retirar_libro(libro))
        except UsuarioError as u:
            print(u)
            raise PrestamoImposibleError()
        except Exception as e:
            print(f"Error desconocido: {e}")
            raise PrestamoImposibleError()

    def cantidad_prestados(self):
        prestados = 0
        for usuario in self.usuarios:
            prestados += usuario.cantidad_prestados()
        return prestados
