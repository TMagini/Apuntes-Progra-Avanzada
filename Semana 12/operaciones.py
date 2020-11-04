class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return self.nombre

class Nodo:

    def __init__(self, valor):
        self.valor = valor
        
    def __repr__(self):
        return repr(self.valor)

class Grafo:

    def __init__(self, lista_adyacencia=None):
        self.lista_adyacencia = lista_adyacencia or {}

    def adyacentes(self, x, y):
        return y in self.lista_adyacencia[x]

    def vecinos(self, x):
        return self.lista_adyacencia[x]

    def agregar_vertice(self, x):
        self.lista_adyacencia[x] = set()

    def remover_vertice(self, x):
        self.lista_adyacencia.pop(x, None)
        for k, v in self.lista_adyacencia.items():
            if x in v:
                v.remove(x)

    def agregar_arista(self, x, y):
        if x in self.lista_adyacencia:
            self.lista_adyacencia[x].add(y)

    def remover_arista(self, x, y):
        vecinos_x = self.lista_adyacencia.get(x, set())
        if y in vecinos_x:
            vecinos_x.remove(y)

    def __repr__(self):
        texto_nodos = []
        for nodo, vecinos in self.lista_adyacencia.items():
            texto_nodos.append(f"Amigos de {nodo}: {vecinos}.")
        return "\n".join(texto_nodos)

# Creamos a nuestros ayudantes y los guardamos en nodos.
bamavrakis = Nodo(Persona("Bastián", 15))
fvr1 = Nodo(Persona("Florencia V", 20))
aaossa = Nodo(Persona("Antonio", 21))
flobarrios = Nodo(Persona("Florencia B", 20))
mjjunemann = Nodo(Persona("Matías", 20))
fgvenegas = Nodo(Persona("Freddie", 10))
indonoso = Nodo(Persona("Ivania", 22))

# Definimos las amistades.
amistades = {
    bamavrakis: set([fvr1, aaossa, flobarrios, mjjunemann, fgvenegas, indonoso]),
    fvr1: set([flobarrios, fgvenegas, indonoso]),
    aaossa: set([fvr1, mjjunemann, indonoso]),
    mjjunemann: set([aaossa, fgvenegas]),
    flobarrios: set([fvr1, aaossa, mjjunemann, indonoso]),
    indonoso: set([fvr1, aaossa, flobarrios, fgvenegas])
}

grafo = Grafo(amistades)
print(grafo)

# ¡Rayos! Nos olvidamos de un ayudante...
# Siempre nos olvidamos de Freddie :(
grafo.agregar_vertice(fgvenegas)
print(f"Amigos de Freddie: {grafo.vecinos(fgvenegas)}")

# Freddie dice que tiene algunos amigos.
grafo.agregar_arista(fgvenegas, aaossa)
grafo.agregar_arista(fgvenegas, bamavrakis)
print(f"Amigos de Freddie: {grafo.vecinos(fgvenegas)}")

# Y Jüne dice que Freddie es su amigo.
grafo.agregar_arista(mjjunemann, fgvenegas)