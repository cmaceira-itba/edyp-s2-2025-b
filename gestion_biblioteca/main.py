from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

if __name__ == "__main__":
    print("Gestion de bibloteca")
    bibl = Biblioteca("Alejandria")
    print(bibl.get_nombre())
    print(bibl.get_libros())
    principito = Libro("El principito")
    libro_2 = Libro("La divina comedia")
    libro_3 = Libro("El principito")

    print(libro_2.titulo)
    print(libro_3.titulo)
    bibl.agregar_libro(principito)
    bibl.agregar_libro(libro_2)
    bibl.agregar_libro(libro_3)
    print("Comparo principito")
    print(principito is libro_3)
    print(principito == libro_3) # __eq__(principito, libro_3) principito.__eq__(libro_3)
    print(bibl.get_libros())
    print(bibl.cantidad_libros())
    paco = Usuario("Paco")
    bibl.agregar_usuario(paco)
    print(bibl.get_usuarios())
    bibl.prestar_libro(paco, principito)
    bibl.prestar_libro(paco, principito)
    print(paco.libros_prestados)
    print(bibl.cantidad_libros())
    print(bibl.cantidad_prestados())
