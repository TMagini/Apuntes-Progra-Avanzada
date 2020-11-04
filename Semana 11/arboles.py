from textwrap import indent
from collections import deque

class Arbol:
    """
    Esta clase representa un árbol
    
    La estructura es recursiva, de manera que cada nodo es la raíz de un sub-árbol.
    Los nodos hijos pueden ser guardados en una estructura, como lista o diccionario.
    En este ejemplo, los nodos hijos serán guardados en un diccionario.
    """

    def __init__(self, id_nodo, valor=None, padre=None):
        """
        Inicializa la estructura básica del árbol.
        
        Tiene un identificador propio, la referencia a su padre, el valor almacenado
        y una estructura con sus hijos.
        """
        self.id_nodo = id_nodo
        self.padre = padre
        self.valor = valor
        self.hijos = {}
        

    def obtener_nodo(self, id_nodo):
        """
        Obtiene el nodo con el id dado, en forma recursiva
        
        A partir del nodo actual, buscamos el nodo 'id_nodo' entre sus hijos
        y lo retornamos si existe.
        """
        # Caso base: ¡Lo encontramos!
        if self.id_nodo == id_nodo:
            return self

        # Buscamos recursivamente entre los hijos
        for hijo in self.hijos.values():
            nodo = hijo.obtener_nodo(id_nodo)
            # Si lo encontró, lo retornamos
            if nodo is not None:
                return nodo
        
        # Si no lo encuentra, retorna None
        return None


    def agregar_nodo(self, id_nodo, valor, id_padre):
        """Agrega un nodo con el id y valor dado, como hijo del nodo con el id 'id_padre'"""
        # Primero, tenemos que encontrar al padre
        padre = self.obtener_nodo(id_padre)
        # En caso de que el padre no exista no hacemos nada
        if padre is None:
            return
        
        # Creamos el nodo
        # Nos aseguramos de que el nodo nuevo sea del mismo tipo que la raíz
        # La siguiente línea es equivalente a Arbol(id_nodo, valor, padre) por ahora
        nodo = type(self)(id_nodo, valor, padre) # Esto lo ocuparemos cuando sea otra clase que herede de Arbol
        # Agregamos el nodo como hijo de su padre
        padre.hijos[id_nodo] = nodo
        
        
    def __repr__(self):
        """
        Entrega una representación del árbol, en forma recursiva.
        
        Para ello, tenemos que pedir la representación de cada hijo recursivamente. 
        Esto nos lleva a recorrer todos los nodos del árbol.
        """
        # Texto de este nodo.
        texto = f"id: {self.id_nodo}, valor: {self.valor}"
        # Si el nodo es hoja, se avisa de ello.
        # Si el nodo no es hoja, se deja un salto de línea para poder nombrar a los hijos.
        texto += ', nodo hoja' if len(self.hijos) == 0 else '\n'

        # Extrae el repr a cada hijo, en forma recursiva.
        repr_hijos = [repr(hijo) for hijo in self.hijos.values()]
        
        # Indentamos cada línea del texto de los hijos con tres espacios.
        # Esto es para que se note el nivel del nodo.
        texto_hijos = [indent(texto_hijo, "   ") for texto_hijo in repr_hijos]
        
        # Usamos join para juntar todos los strings anteriores con un salto de línea entre cada uno.
        return texto + "\n".join(texto_hijos)

'''
T = Arbol(0, 10)
T.agregar_nodo(1, 8, 0)
T.agregar_nodo(3, 12, 0)
T.agregar_nodo(2, 9, 1)
T.agregar_nodo(4, 5, 3)
T.agregar_nodo(5, 14, 3)
T.agregar_nodo(6, 20, 3)
T.agregar_nodo(8, 4, 2)
T.agregar_nodo(7, 8, 4)
T.agregar_nodo(9, 15, 6)
T.agregar_nodo(10, 6, 6)

print(T)
'''

class ArbolBFS(Arbol):
    """Heredamos de la clase Arbol para hacerla iterable según el orden con BFS"""
    
    def __iter__(self):
        """Recorre el árbol según BFS"""
        
        # Utilizamos una cola para almacenar los nodos por visitar
        cola = deque()

        # El primer nodo a visitar será la raíz
        cola.append(self)

        # Mientras queden nodos por visitar en la cola
        while len(cola) > 0:
            
            # Extraemos el primero de la cola
            nodo_actual = cola.popleft() 
            # Entregamos el nodo actual que se recorre
            yield nodo_actual

            # Agregamos todos los nodos hijos a la cola
            for hijo in nodo_actual.hijos.values():
                cola.append(hijo)

T = ArbolBFS(0, 10)
T.agregar_nodo(1, 8, 0)
T.agregar_nodo(3, 12, 0)
T.agregar_nodo(2, 9, 1)
T.agregar_nodo(4, 5, 3)
T.agregar_nodo(5, 14, 3)
T.agregar_nodo(6, 20, 3)
T.agregar_nodo(8, 4, 2)
T.agregar_nodo(7, 8, 4)
T.agregar_nodo(9, 15, 6)
T.agregar_nodo(10, 6, 6)

for nodo in T:
    print(f"Visitando nodo de id: {nodo.id_nodo}")


class ArbolDFSRecursivo(Arbol):
    """Heredamos de la clase Arbol para hacerla iterable según el orden con DFS recursivo"""
    
    def __iter__(self):
        """Recorrde el árbol según DFS recursivo"""
        
        # Visitamos el nodo actual
        yield self
        
        # Aplicamos esto recursivamente a cada subarbol
        for subarbol in self.hijos.values():
            yield from subarbol

for nodo in T:
    print(f"Visitando nodo de id: {nodo.id_nodo}")