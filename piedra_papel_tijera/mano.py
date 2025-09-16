from random import choice, random

class OpcionesEnum:
    PIEDRA = "PIEDRA"
    PAPEL = "PAPEL"
    TIJERA = "TIJERA"
    OPCIONES = [PIEDRA, PAPEL, TIJERA]

class Mano:

    opciones = OpcionesEnum.OPCIONES

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = None

    def seleccionar(self):
        self.estado = choice(Mano.opciones)

    def mostrar(self):
        return self.estado

    def get_nombre(self):
        return self.nombre

    def __str__(self):
        if not self.estado:
            return "La mano no jugo"
        else:
            return f"La mano tiene {self.estado}"


class ManoNene(Mano):
    def seleccionar(self):
        eleccion = random() * 100
        if eleccion >= 20:
            self.estado = OpcionesEnum.PIEDRA
        elif eleccion < 10:
            self.estado = OpcionesEnum.TIJERA
        else:
            self.estado = OpcionesEnum.PAPEL

class ManoTerca(Mano):
    def seleccionar(self):
        self.estado = OpcionesEnum.PAPEL
