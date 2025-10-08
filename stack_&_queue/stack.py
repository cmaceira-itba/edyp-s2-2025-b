from typing import Any, Optional
from nodo import Nodo

class Stack:
    def __init__(self):
        self.top: Optional[Nodo] = None
        self.length: int = 0

    def push(self, dato: Any):
        new: Nodo = Nodo(dato=dato)
        if not self.top:
            self.top = new
        else:
            self.top.set_sig(new)
            new.set_ant(self.top)
            self.top = new
        self.length += 1

    def pop(self):
        if not self.top:
            return None
        dato = self.top.get_dato()
        if len(self) == 1:
            self.top = None
            self.length -= 1
            return dato
        self.top = self.top.get_ant()
        if self.top : self.top.set_sig(None)
        self.length -= 1
        return dato

    def __len__(self):
        return self.length

    def __str__(self):
        aux = self.top
        string = "["
        if aux:
            while aux.get_ant() != None:
                string += str(aux.get_dato())
                if aux.get_ant() != None:
                    string += ", "
                aux = aux.get_ant()
        string += "]"
        return string


def validar_parentesis(parentesis: str):
    pila = Stack()
    invalida = False
    for p in parentesis:
        if p == "(":
            pila.push(p)
        elif p == ")" and len(pila) == 0:
            invalida = True
            pila.pop()
        else:
            pila.pop()
    if pila.length == 0 and not invalida:
        print("Balanceados!")
    else:
        print("Desbalanceados")
    print(pila)


if __name__ == "__main__":
    validar_parentesis("()((()))()")
    validar_parentesis(")()()(")
    validar_parentesis(")))))))))))))))")
