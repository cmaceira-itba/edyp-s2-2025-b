
class Camion:
    patentes_usadas = []

    def __init__(self, patente):
        self.patente = None
        if patente in Camion.patentes_usadas:
            raise ValueError("La patente ya fue usada")
        self.patente = patente
        Camion.patentes_usadas.append(patente)

    def __del__(self):
        if self.patente:
            Camion.patentes_usadas.remove(self.patente)

    def __eq__(self, other):
        try:
            return self.patente == other.patente
        except:
            return False
