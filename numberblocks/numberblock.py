class Numberblock:
    instancias = {}

    @classmethod
    def agregar(cls, numberblock):
        if cls.instancias.get(numberblock.numero):
            cls.instancias[numberblock.numero].append(numberblock)
            return

        cls.instancias[numberblock.numero] = [numberblock]


    def validar_numero(self, numero):
        if numero <= 0:
            raise ValueError("No puedo ser negativo")
        return numero

    def __init__(self, numero):
        self.numero = self.validar_numero(numero)
        Numberblock.agregar(self)

class Rebelblock(Numberblock):
    # Si no tiene init mi subclase usa directamente la del padre
    # Mi subclase sobreescribe validar_numero y eso cambia el comportamiento
    # de la clase padre
    def validar_numero(self, numero):
        if numero >= 0:
            raise ValueError("No puedo ser positivo")
        return numero

    def replicar(self):
        raise NotImplementedError("No puedo replicarme")


if __name__ == "__main__":
    try:
        number_valido = Numberblock(10)
        number_invalido = Numberblock(-1)
    except ValueError as e:
        print("No se creo el number_invalido", e)

    print(number_valido.numero)

    rebel = Rebelblock(-1)
    rebel.replicar()
