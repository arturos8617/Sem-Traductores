class ElementoPila:
    def muestra(self):
        pass

class Terminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def muestra(self):
        return self.simbolo

class NoTerminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def muestra(self):
        return self.simbolo

class Estado(ElementoPila):
    def __init__(self, estado):
        self.estado = estado

    def muestra(self):
        return f"Estado {self.estado}"

class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def top(self):
        return self.elementos[-1] if self.elementos else None

    def muestra(self):
        return ' '.join([elem.muestra() for elem in reversed(self.elementos)])

# Ejemplo de uso
pila = Pila()
pila.push(Estado(0))
pila.push(Terminal('a'))
pila.push(Terminal('+'))
pila.push(Terminal('b'))
pila.push(Estado(4))

print(pila.muestra())  # Muestra el estado actual de la pila
