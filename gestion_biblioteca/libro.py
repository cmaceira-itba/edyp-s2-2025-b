class Libro:
    """Representa un libro con titulo, autor, isbn y editorial.
    Cada instancia de libro es unica en la biblioteca, representa un ejemplar."""
    
    @staticmethod
    def _validar_titulo(titulo):
        if not titulo:
            raise ValueError("Titulo no puede estar vacio")
        if not isinstance(titulo, str):
            raise TypeError("Debe ser string")
        return titulo

    @staticmethod
    def _validar_autor(autor):
        if not autor:
            raise ValueError("Autor no puede estar vacio")
        if not isinstance(autor, str):
            raise TypeError("Debe ser string")
        return autor

    @staticmethod
    def _validar_isbn(isbn):
        if not isbn:
            raise ValueError("ISBN no puede estar vacio")
        if not isinstance(isbn, str):
            raise TypeError("Debe ser string")
        return isbn

    @staticmethod
    def _validar_editorial(editorial):
        if not editorial:
            raise ValueError("Editorial no puede estar vacio")
        if not isinstance(editorial, str):
            raise TypeError("Debe ser string")
        return editorial

    def __init__(self, titulo, autor, isbn, editorial):
        self.autor = Libro._validar_autor(autor)
        self.titulo = Libro._validar_titulo(titulo)
        self.isbn = Libro._validar_isbn(isbn)
        self.editorial = Libro._validar_editorial(editorial)

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_editorial(self):
        return self.editorial

    def __str__(self):
        return f"Libro: {self.titulo} de {self.autor}"

    def __repr__(self):
        return self.titulo + " - " + self.autor

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        if self.titulo != other.titulo:
            return False
        if self.edicion != other.edicion:
            return False
        if self.isbn != other.isbn:
            return False
        if self.autor != other.autor:
            return False
        if self.editorial != other.editorial:
            return False
        return True
