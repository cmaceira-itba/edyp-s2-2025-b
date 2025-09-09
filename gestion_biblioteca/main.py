from biblioteca import Biblioteca, BibliotecaError
from libro import Libro
from usuario import UsuarioBasico

if __name__ == "__main__":
    print("Gestion de bibloteca")
    bibl = Biblioteca("Alejandria")
    print(bibl.get_nombre())
    print(bibl.get_libros())
    libro_1 = Libro("El principito")
    libro_2 = Libro("La divina comedia")
    libro_3 = Libro("El Eternauta")
    bibl.agregar_libro(libro_1)
    bibl.agregar_libro(libro_2)
    bibl.agregar_libro(libro_3)
    print(bibl.ejemplares_por_titulo)
    print(bibl.get_libros_ordenados())
    print(bibl.get_libros())
    print(bibl.cantidad_libros())

    paco = UsuarioBasico("Paco")
    try:
        bibl.agregar_usuario(paco)
    except BibliotecaError as b:
        print(b)
    except Exception as e:
        print(e)


    print(bibl.get_usuarios())
    print(bibl.get_libros())
    #bibl.prestar_libro(paco, libro_1)
    bibl.prestar_libro(paco, libro_2)
    print(bibl.get_libros())
