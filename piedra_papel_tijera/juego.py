from mano import OpcionesEnum

class Juego:
    EMPATE = "empate"
    reglas = {
        (OpcionesEnum.PIEDRA, OpcionesEnum.TIJERA): OpcionesEnum.PIEDRA,
        (OpcionesEnum.PAPEL, OpcionesEnum.PIEDRA):OpcionesEnum.PAPEL,
        (OpcionesEnum.TIJERA,OpcionesEnum.PAPEL): OpcionesEnum.TIJERA
    }

    def __init__(self, jugador_1, jugador_2):
        self.jugador_1 = jugador_1
        self.jugador_2 = jugador_2
        self.jugadas = []
        self.contador = 1

    def jugar(self):
        self.jugador_1.seleccionar()
        self.jugador_2.seleccionar()

        jugada = (self.jugador_1.mostrar(), self.jugador_2.mostrar())

        resultado = [self.contador, jugada[0], jugada[1]]

        if jugada[0] == jugada[1]:
            resultado.append(Juego.EMPATE)
        elif Juego.reglas.get(jugada):
            resultado.append(self.jugador_1.get_nombre())
        else:
            resultado.append(self.jugador_2.get_nombre())

        self.jugadas.append(resultado)

        self.contador += 1
