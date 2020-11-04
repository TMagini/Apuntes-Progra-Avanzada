# Representación con nodos

class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []
        
    def agregar_vecino(self, nodo):
        self.vecinos.append(nodo)
        
    def __repr__(self):
        texto = f"[{self.valor}]"
        if len(self.vecinos) > 0:
            textos_vecinos = [f"[{vecino.valor}]" for vecino in self.vecinos]
            texto += " -> " + ", ".join(textos_vecinos)
        return texto

nodo_1 = Nodo(1)
nodo_2 = Nodo(2)
nodo_3 = Nodo(3)
nodo_4 = Nodo(4)
nodo_5 = Nodo(5)

nodo_1.agregar_vecino(nodo_2)
nodo_2.agregar_vecino(nodo_3) 
nodo_3.agregar_vecino(nodo_2) 
nodo_3.agregar_vecino(nodo_4)
nodo_3.agregar_vecino(nodo_5) 
nodo_4.agregar_vecino(nodo_5)

print(nodo_1)
print(nodo_2)
print(nodo_3)
print(nodo_4)
print(nodo_5)

# Lista de adyacencia

# Aquí usamos diccionarios con llave: int y valor: list porque ofrece más facilidad de búsqueda.
# Cada llave del diccionario es el valor de un vertice, y el valor asociado es la lista de vertices con conexión.
# También podrían ser list(tuple(int, list)). ¿Por qué no sería correcto hacer list(list(int, list))?

grafo_no_dirigido = {1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5], 5: [3, 4]}
grafo_dirigido = {1: [2], 2: [3], 3: [2, 4, 5], 4: [5], 5: []}

# ¿Vértices del grafo?
print(list(grafo_no_dirigido.keys()))

# ¿Vecinos de vértice 3 en grafo no dirigido?
print(grafo_no_dirigido[3])

# Matriz de adyacencia

grafo_no_dirigido = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]
grafo_dirigido    = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]

for fila in grafo_no_dirigido:
    print(fila)

for fila in grafo_dirigido:
    print(fila)