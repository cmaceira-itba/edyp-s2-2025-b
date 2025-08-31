class Libro:

    def __init__(self, titulo):
        self.titulo = titulo
        self.edicion = "1er"

    def __eq__(self, other):
        print("Comparo libros!")
        if not isinstance(other, Libro):
            return False
        if self.titulo != other.titulo:
            return False
        if self.edicion != other.edicion:
            return False
        return True
