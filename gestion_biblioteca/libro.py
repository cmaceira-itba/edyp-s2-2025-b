class Libro:

    @staticmethod
    def _validar_titulo(titulo):
        if not titulo:
            raise ValueError("Titulo no puede estar vacio")
        if not isinstance(titulo, str):
            raise TypeError("Debe ser string")
        return titulo

    def _validar_edicion(edicion):
        if not edicion:
            raise ValueError("Edicion no puede ser nulo")
        if not isinstance(edicion, int):
            raise ValueError("Edicion debe ser entero")
        return edicion
    
    def __init__(self, titulo):
        self.titulo = Libro._validar_titulo(titulo)
        self.edicion = "1er"

    def __str__(self):
        return f"Libro: {self.titulo}"

    def __repr__(self):
        return self.titulo

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        if self.titulo != other.titulo:
            return False
        if self.edicion != other.edicion:
            return False
        return True
