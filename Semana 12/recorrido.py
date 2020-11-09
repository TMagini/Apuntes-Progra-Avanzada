from collections import deque

# Utilizaremos estas definiciones para Persona, Nodo y para Grafo, que ya habíamos revisado anteriormente.
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
    

## Y creamos algunos nodos, y un grafo de amistades
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
    indonoso: set([fvr1, aaossa, flobarrios, fgvenegas]),
    fgvenegas: set([aaossa, bamavrakis])
}

grafo = Grafo(amistades)
print(grafo)

# BFS

def bfs(grafo, inicio):
    # Vamos a mantener una lista con los nodos visitados.
    visitados = []
    # La cola de siempre, comienza desde el nodo inicio.
    queue = deque([inicio])
    
    while len(queue) > 0:
        vertice = queue.popleft()
        # Detalle clave: si ya visitamos el nodo, no hacemos nada!
        if vertice in visitados:
            continue

        # Lo visitamos
        print(vertice)
        visitados.append(vertice)
        # Agregamos los vecinos a la cola si es que no han sido visitados.
        for vecino in grafo[vertice]:
            if vecino not in visitados:
                queue.append(vecino)
    return visitados

bfs(amistades, bamavrakis)

# DFS

def dfs(grafo, inicio):
    # Vamos a mantener un set con los nodos visitados.
    visitados = set()

    # El stack de siempre, comienza desde el nodo inicio.
    stack = [inicio]

    while len(stack) > 0:
        vertice = stack.pop()
        # Detalle clave: si ya visitamos el nodo, ¡no hacemos nada!
        if vertice in visitados:
            continue

        # Lo visitamos
        print(vertice)
        visitados.add(vertice)

        # Agregamos los vecinos al stack si es que no han sido visitados.
        for vecino in grafo[vertice]:
            if vecino not in visitados:
                stack.append(vecino)

    return list(visitados)

dfs(amistades, bamavrakis)

def dfs_recursivo(grafo, vertice, visitados=None):
    visitados = visitados or set()

    # Lo visitamos
    print(vertice)
    visitados.add(vertice)

    for vecino in grafo[vertice]:
        # Detalle clave: si ya visitamos el nodo, ¡no hacemos nada!
        if vecino not in visitados:
            dfs_recursivo(grafo, vecino, visitados)

    return list(visitados)

dfs_recursivo(amistades, bamavrakis)