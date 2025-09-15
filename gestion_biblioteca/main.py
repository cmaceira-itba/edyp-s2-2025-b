
from biblioteca import Biblioteca, BibliotecaError
from libro import Libro
from usuario import UsuarioBasico
from aplicacion import AplicacionBiblioteca

if __name__ == "__main__":
    print("Gestion de biblioteca")
    bibl = Biblioteca("Alejandria")
    # Libros de ejemplo
    libro_1 = Libro("El principito", "Antoine de Saint-Exupéry", "978-3-16-148410-0", "Reynal & Hitchcock")
    libro_2 = Libro("La divina comedia", "Dante Alighieri", "978-3-16-148410-1", "Gutenberg")
    libro_3 = Libro("El Eternauta", "Héctor Germán Oesterheld", "978-3-16-148410-2", "Editorial Frontera")
    bibl.agregar_libro(libro_1)
    bibl.agregar_libro(libro_2)
    bibl.agregar_libro(libro_3)
    # Usuario de ejemplo
    paco = UsuarioBasico("Paco", "12345678")
    try:
        bibl.agregar_usuario(paco)
    except BibliotecaError as b:
        print(b)
    except Exception as e:
        print(e)

    # Lanzar la aplicación interactiva
    app = AplicacionBiblioteca(bibl)
    app.ejecutar()
