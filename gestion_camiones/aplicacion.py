from camion import Camion

class AplicacionGestionFlota:
    """Separa la logica del camion del uso que le vamos
    a dar en el programa."""
    
    def __init__(self):
        self.galpon_camiones = []
        self.opciones = {
            "1": "Agregar un camion",
            "2": "Mostrar camiones",
            "0": "Salir"
        }

    def mostrar_opciones(self):
        for k, v in self.opciones.items():
            print(f"{k}: {v}")

    def menu(self):
        print("Aplicacion de camiones: ")
        opcion = ""
        while opcion != "0":
            self.mostrar_opciones()
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.crear_camion()
            elif opcion == "2":
                self.imprimir_camion()
            elif opcion == "0":
                print("Adios!")
            else:
                print("Opcion invalida")

    def crear_camion(self):
        camion = None
        try:
            patente = input("Ingrese una patente: ")
            if not patente:
                print("No puede se patente vacia")
                return
            camion = Camion(patente)
        except Exception as e:
            print(e)
        if camion:
            self.galpon_camiones.append(camion)

    def imprimir_camion(self):
        for camion in self.galpon_camiones:
            print(camion)
