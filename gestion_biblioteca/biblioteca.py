from libro import Libro
from usuario import Usuario, UsuarioError

class Biblioteca:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ejemplares_por_titulo = {}
        self.usuarios = []

    def get_nombre(self):
        return self.nombre

    @property
    def libros(self):
        return self.get_libros()

    def get_libros(self):
        libros = []
        for ejemplares in self.ejemplares_por_titulo.values():
            for ejemplar in ejemplares:
                libros.append(ejemplar)
        return libros

    def get_titulos(self):
        return self.ejemplares_por_titulo.keys()

    def get_libros_ordenados(self):
        return sorted(self.get_libros(), key=lambda x: x.titulo)

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("No es un Libro")
        if not self.ejemplares_por_titulo.get(libro.titulo):
            self.ejemplares_por_titulo[libro.titulo] = [libro]
            return
        if libro in self.ejemplares_por_titulo[libro.titulo]:
            raise LibroRepetidoError()
        self.ejemplares_por_titulo[libro.titulo].append(libro)

    def cantidad_libros(self):
        return len(self.get_libros())

    def cantidad_titulos(self):
        return len(self.ejemplares_por_titulo.keys())

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
        if not isinstance(libro, Libro):
            raise TypeError("No es un libro")
        titulo_buscado = libro.titulo
        if not self.ejemplares_por_titulo.get(titulo_buscado):
            raise LibroNoPerteneceError()
        if len(self.ejemplares_por_titulo[titulo_buscado]) == 0:
            raise LibroNoDisponible()
        return self.ejemplares_por_titulo[titulo_buscado].pop()

    def validar_usuario_socio(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("No es un Usuario")
        # No puedo prestar un libro a un usuario que no pertenece a la bibl
        if usuario not in self.usuarios:
            raise UsuarioNoPerteneceError()

    def validar_libro(self, libro):
        if not isinstance(libro, Libro):
            raise TypeError("No es un Libro")
        # No puedo prestar un libro a un usuario que no pertenece a la bibl
        if libro not in self.libros:  # PUEDO HACER ESTO PORQUE TENGO @property
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

class LibroNoDisponible(BibliotecaError):
    def __init__(self):
        super().__init__("No hay ejemplares disponibles del libro")

class PrestamoImposibleError(BibliotecaError):
    def __init__(self):
        super().__init__("El prestamo no es posible")
