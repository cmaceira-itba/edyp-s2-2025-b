from mano import Mano, ManoNene, ManoTerca
from juego import Juego
from guardar import GuardarJugadas

if __name__ == "__main__":

    hno_pepe = ManoNene("Pepito")

    hno_sofia = ManoTerca("Pachi")

    juego = Juego(hno_sofia, hno_pepe)

    for _ in range(10):
        juego.jugar()

    guardador = GuardarJugadas()
    print(juego.jugadas)
    guardador.guardar(juego.jugadas)

    # Tarea: Quien gano mas veces?
