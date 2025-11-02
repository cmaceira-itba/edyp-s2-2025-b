from collections import deque

class NaveEspacial:
    AGREGAR = "agregar"
    REMOVER = "remover"
    def __init__(self):
        self._recorrido = deque() # Tomo como cola popleft <----< append
        self._historial_acciones = deque() # Tomo como pila appendleft popleft ><----

    def agregar_coordenada(self, coordenada):
        """
        Añade una nueva coordenada visitada.
        :param coordenada: tupla con (x, y, z)
        """
        # Completar: agregar coordenada al recorrido y registrar acción para posible
        self._recorrido.append(coordenada)
        self._historial_acciones.appendleft((NaveEspacial.AGREGAR, coordenada))

    def remover_coordenada(self):
        coordenada = self._recorrido.popleft()
        self._historial_acciones.appendleft((NaveEspacial.REMOVER, coordenada))
        return coordenada

    def obtener_recorrido(self):
        """Devuelve la secuencia de coordenadas visitadas en orden."""
        print(self._recorrido)
        return list(self._recorrido)

    def deshacer_maniobra(self):
        """
        Revierten la última maniobra y actualiza el recorrido.
        """
        print(self._historial_acciones)
        maniobra = self._historial_acciones.popleft()
        if maniobra[0] == NaveEspacial.AGREGAR:
            nuevo_recorrido = deque()
            coordenada = self._recorrido.popleft()
            while coordenada != maniobra[1]:
                nuevo_recorrido.append(coordenada)
                coordenada = self._recorrido.popleft()
            self._recorrido = nuevo_recorrido

        elif maniobra[0] == NaveEspacial.REMOVER:
            self._recorrido.appendleft(maniobra[1])


if __name__ == "__main__":
    nave = NaveEspacial()
    nave.agregar_coordenada((0,0,0))
    nave.agregar_coordenada((1,1,1))
    nave.agregar_coordenada((2,2,2))

    print("Caso 1")
    print(nave.obtener_recorrido() == [(0,0,0),(1,1,1),(2,2,2)])

    nave.deshacer_maniobra()

    print("Caso 2")
    print(nave.obtener_recorrido() == [(0,0,0),(1,1,1)])

    nave.agregar_coordenada((3,3,3))
    nave.deshacer_maniobra()
    nave.agregar_coordenada((4,4,4))

    print("Caso 3")
    print(nave.obtener_recorrido() == [(0,0,0),(1,1,1),(4,4,4)])

    print("Caso 4")
    print(nave.remover_coordenada() ==  (0,0,0))
    nave.deshacer_maniobra()
    print(nave.obtener_recorrido() == [(0,0,0),(1,1,1),(4,4,4)])

    print("Caso 5")
    nave.deshacer_maniobra()
    print(nave.obtener_recorrido())
