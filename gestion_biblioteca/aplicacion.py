from libro import Libro
from usuario import UsuarioBasico

class AplicacionBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def mostrar_menu(self):
        print("\n--- Menú de la Biblioteca ---")
        print("1. Mostrar nombre de la biblioteca")
        print("2. Listar libros")
        print("3. Agregar libro")
        print("4. Listar usuarios")
        print("5. Agregar usuario")
        print("6. Prestar libro")
        print("7. Devolver libro")
        print("8. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                print(self.biblioteca.get_nombre())
            elif opcion == "2":
                print(self.biblioteca.get_libros())
            elif opcion == "3":
                self.agregar_libro()
            elif opcion == "4":
                print(self.biblioteca.get_usuarios())
            elif opcion == "5":
                self.agregar_usuario()
            elif opcion == "6":
                self.prestar_libro()
            elif opcion == "7":
                self.devolver_libro()
            elif opcion == "8":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

    def agregar_libro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        isbn = input("ISBN: ")
        editorial = input("Editorial: ")
        libro = Libro(titulo, autor, isbn, editorial)
        self.biblioteca.agregar_libro(libro)
        print("Libro agregado.")

    def agregar_usuario(self):

        nombre = input("Nombre: ")
        dni = input("DNI: ")
        usuario = UsuarioBasico(nombre, dni)
        try:
            self.biblioteca.agregar_usuario(usuario)
            print("Usuario agregado.")
        except Exception as e:
            print(f"Error: {e}")

    def prestar_libro(self):
        dni = input("DNI del usuario: ")
        titulo = input("Título del libro: ")
        usuario = next((u for u in self.biblioteca.get_usuarios() if getattr(u, 'dni', None) == dni), None)
        libro = next((l for l in self.biblioteca.get_libros() if getattr(l, 'titulo', None) == titulo), None)
        if usuario and libro:
            try:
                self.biblioteca.prestar_libro(usuario, libro)
                print("Libro prestado.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self):
        dni = input("DNI del usuario: ")
        titulo = input("Título del libro: ")
        usuario = next((u for u in self.biblioteca.get_usuarios() if getattr(u, 'dni', None) == dni), None)
        libro = next((l for l in self.biblioteca.get_libros() if getattr(l, 'titulo', None) == titulo), None)
        if usuario and libro:
            try:
                self.biblioteca.devolver_libro(usuario, libro)
                print("Libro devuelto.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Usuario o libro no encontrado.")
