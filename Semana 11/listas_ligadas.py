class Nodo:
    """Esta clase representa un nodo de una lista ligada"""
    def __init__(self, valor=None):
        """Inicializa la estructura del nodo"""
        self.valor = valor
        self.siguiente = None # Al crear un nodo, la referencia al siguiente nodo comienza vacía.

class ListaLigada:
    """Clase que representa una lista ligada"""

    
    def __init__(self):
        """Inicializa una lista ligada vacia, con una referencia nula a su cabeza y cola"""
        self.cabeza = None
        self.cola = None

        
    def agregar(self, valor):
        """Agrega un nodo al final de la cola, similar a lista.append"""
        # Inicializamos el nuevo nodo
        nuevo = Nodo(valor)
        # Si la lista está vacía (no hay cabeza)
        if self.cabeza is None:
            # El nuevo nodo es la cabeza y el nodo cola de la lista
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            # Agregamos el nuevo nodo como sucesor del nodo cola actual.
            self.cola.siguiente = nuevo
            # Actualizamos la referencia al nodo cola.
            self.cola = self.cola.siguiente

            
    def obtener(self, posicion):
        """Busca el valor del nodo que está en la posición indicada, partiendo de 0"""
        # Empezamos en la cabeza
        nodo_actual = self.cabeza

        # Recorremos secuencialmente la lista ligada siguiendo los punteros
        # al nodo siguiente.
        for _ in range(posicion):
            # Revisamos que no se haya llegado al final de la lista
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente
        
        # Si buscamos una posición mayor a la longitud de la lista ligada
        if nodo_actual is None:
            return None # Retorna "nada"
        return nodo_actual.valor

    
    def insertar(self, valor, posicion):
        """Inserta un valor nuevo en una posición arbitraria"""
        # Inicializamos el nuevo nodo
        nodo_nuevo = Nodo(valor)
        # Empezamos en la cabeza
        nodo_actual = self.cabeza
        
        # Caso particular: insertar en la cabeza
        if posicion == 0:
            # Actualizamos la cabeza
            nodo_nuevo.siguiente = self.cabeza
            self.cabeza = nodo_nuevo
            # Caso más particular. Si la lista estaba vacia, actualizamos la cola
            if nodo_nuevo.siguiente is None:
                self.cola = nodo_nuevo
            # Terminamos de ejecutar la función
            return
        
        # Buscamos el nodo predecesor
        for _ in range(posicion - 1):
            if nodo_actual is not None:
                nodo_actual = nodo_actual.siguiente

        # Si encontramos el predecesor, actualizamos las referencias
        if nodo_actual is not None:
            # Si no lo hacemos en este orden perdemos la referencia
            # al resto de la lista ligada
            nodo_nuevo.siguiente = nodo_actual.siguiente        
            nodo_actual.siguiente = nodo_nuevo
            # Caso particular: si es que insertamos en la última posición
            if nodo_nuevo.siguiente is None:
                self.cola = nodo_nuevo

                
    def __repr__(self):
        """Forma una representación de la lista"""
        string = ""
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            string = f"{string}{nodo_actual.valor} → "
            nodo_actual = nodo_actual.siguiente
        return string


lista = ListaLigada()
print(lista)
lista.agregar(2)
print(lista)
lista.agregar(3)
print(lista)
lista.agregar(5)
print(lista)
lista.agregar(7)
print(lista)
lista.agregar(11.0)
print(lista)

print(f"Posición {2}: {lista.obtener(2)}")
print(f"Posición {1}: {lista.obtener(1)}")

lista.insertar("cuatro", 2)
print(lista)
lista.insertar("cero", 0)
print(lista)
lista.insertar("uno", 1)
print(lista)
lista.insertar("trece", 8)
print(lista)
lista.insertar("veinte", 20)
print(lista)