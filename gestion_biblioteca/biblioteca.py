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
        if libro in self.libros:
            return
        self.libros.append(libro)

    def cantidad_libros(self):
        return len(self.libros)

    def get_usuarios(self):
        return self.usuarios

    def agregar_usuario(self, usuario):
        if usuario in self.usuarios:
            return
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if usuario not in self.usuarios:
            return
        if libro not in self.libros:
            return
        self.libros.remove(libro)
        usuario.pedir_prestado(libro)

    def cantidad_prestados(self):
        prestados = 0
        for usuario in self.usuarios:
            prestados += usuario.cantidad_prestados()
        return prestados
