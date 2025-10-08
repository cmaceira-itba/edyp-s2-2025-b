from typing import Any

class Nodo:
    def __init__(self, dato: Any):
        self.dato = dato
        self.sig = None
        self.ant = None

    def set_sig(self, sig):
        self.sig = sig

    def set_ant(self, ant):
        self.ant = ant

    def get_ant(self):
        return self.ant

    def get_sig(self):
        return self.sig

    def get_dato(self):
        return self.dato
