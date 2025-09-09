class Vehiculo:
    pass

class Terrestre:
    def __init__(self,patente):
        print("Terrestre")
        self.patente = patente + "terrestre"

    def andar(self):
        print("Rodando por La tierra")

class Acuatico:
    def __init__(self, patente):
        print("Acuatico")
        self.patente = patente + "acuatica"

    def andar(self):
        print("No ando por la tierra")

    def navegar(self):
        print("navegando por el agua")


class Anfibio(Terrestre, Acuatico):
    def __init__(self, patente):
        print("Anfibio")
        super().__init__(patente)

    def andar(self):
        super().andar()


if __name__ == "__main__":
    anf = Anfibio("ABC123")
    anf.andar()
    anf.navegar()
    print(anf.patente)
