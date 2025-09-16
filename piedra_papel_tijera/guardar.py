import csv

class GuardarJugadas:
    def guardar(self, jugadas):
        try:
            with open("piedra_papel_tijera/jugadas.csv", "w") as archivo:
                escritor = csv.writer(archivo)
                for resultado in jugadas:
                    escritor.writerow(resultado)

        except Exception:
            print("No se pudo escribir el archivo")
