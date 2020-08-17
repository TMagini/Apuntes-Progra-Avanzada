# Semana 1 | Estructuras de datos

1. [Tuplas](#Tuplas)
2. [Listas (super poco)](#Listas)
3. [Stacks](#Stacks)
4. [Colas (queues)](#Colas-(queues))
5. [Diccionarios](#Diccionarios)
6. [Sets](#Sets)
7. [Args y Kwargs](#Args-y-Kwargs)

## Tuplas

Se utilizan para manejar datos de forma **ordenada** e **inmutable**, en otras palabras no puedo cambiar los valores de una tupla. Funcionan casi igual que las listas con algunas diferencias como:

Cuando se crea una tupla se debe incluir una coma al final o puedo crear una tupla sin tener que definirla con `()`, soporta distintos tipos de elementos.

```python
c = (0, )
d = 0, 'uno'
```

Las tuplas son estructuras de datos **inmutables**. Esto significa que **no es posible agregar o eliminar elementos**, o bien cambiar el contenido de la tupla una vez que ésta fue creada. Lo que si se puede hacer es modificar algún valor contenido _dentro_ de un elemento de la tupla (Ejemplo realizado en contenidos Semana 1).

La tuplas tambien permiten retornar varibles individuales empaquetadas, por ejemplo un función que retorne más de una variable, y estas se pueden desenpaquetar en variables independientes. Por ejemplo:

```python
def calcular_geometria(a, b):
    area = a*b
    perimeter = (2*a) + (2*b)
    mpa = a / 2
    mpb = b / 2
    return (area, perimeter, mpa, mpb) # Empaquetando variables

data = calcular_geometria(20.0, 10.0)

a, p, mpa, mpb = data # Desempaquetando varibales en individuales

a, p, mpa, mpb = calcular_geometria(20.0, 10.0) # Desempaquetar directamente
```

Forma general de hacer slicing en Python:

- ```a[start:end]```: retorna los elementos desde ```start``` hasta ```end - 1```

- ```a[start:]```: retorna los elementos desde ```start``` hasta el final del arreglo

- ```a[:end]```: retorna los elementos desde el principio hasta ```end - 1```

- ```a[:]```: crea una copia (shallow) del arreglo completo. Es decir, el arreglo retornado está en una nueva dirección de memoria, pero los elementos en el arreglo están hace referencia a la dirección de memoria a los elementos del arreglo inicial

- ```a[start:end:step]```: retorna los elementos desde ```start``` hasta no pasar ```end```, en pasos de a ```step```

- ```a[-1]```: retorna el último elemento en el arreglo

- ```a[-n:]```:   # últimos ```n``` elementos en el arreglo

- ```a[:-n]```: retorna todos los elementos del arreglo menos los últimos ```n``` elementos

- `a[::-1]`: invierte la tupla

### Named tuples

Revisar en contenidos Semana 1

## Listas

Si quiero agreagr los elementos de una lista a otra listas estilo:

```python
bandas = ['Radiohead', 'City and Colour', 'toe'] # Le quiero agregar nuevas_bandas

nuevas_bandas = ['Young the Giant', 'Portugal. The Man', 'Twenty One Pilots']
```

Aplico `.extend()` y me agrega en el mismo orden pero como variables, no como listas, sin tener que utilizar el `.append()` para cada uno de los elementos.

```python
bandas = ['Radiohead', 'City and Colour', 'toe', 'Young the Giant', 'Portugal. The Man', 'Twenty One Pilots']
```

### Listas de compresión

Las listas por comprensión se pueden ver como listas formadas por un conjunto de objetos que cumplen con un concepto o condición en particular, por ejemplo con el la lista `bandas`, quiero una lista que me de el `len()` de cada uno de sus elementos, con lo que utilizamos:

```python
largo_de_bandas = [len(nombre) for nombre in bandas]
```

retornadno `[9, 19, 15, 3, 15, 17, 17]`, también a estas listas de compresión se les puede colocar condiciones tales como, quiero una lista de las bandas que tengas un **largo menor a 10 caracteres**:

`nueva_lista = [expresión for elemento in lista/iterador if condicion/condiciones]`

```python
bandas_con_nombre_corto = [nombre for nombre in bandas if len(nombre) < 10]
```

Para el ordenamiento de listas existe el `.sort()` el cual se utiliza como función, estilo tengo una lista y le pongo el `.sort()` y me devuelve la lista ordenada de menor a mayor, esta por ende no se puede almacenar en ningnuna variable, solo se le llama, en cambio el `sorted()` se utiliza poniendo como parámetro la lista y esta no modifica la original y se puede guardar en una variable, dando la opción de tener la misma lista 2 veces solo que en una esta la original (desordenada) y en la otra esta la ordenada. (Para cambiar el orden de mayor a menor en el `.sorted(reverse=True)` basta con poner eso de parámetro).

## Stacks

Es una estructura de datos que funciona como una pila de objetos, se van almacenando obejtos unos encima de otros, tal como una pila de platos, y cuando queremos sacar algo, sacamos uno de arriba de la pila, por ende se saca siempre el último.

Las operaciones basicas son:

- ***Push***: Agregar elemnto al tope del stack (`.append()`)
- ***Pop***: Eliminar el elemento del tope del stack (siempre sacará el último que se haya agregado), y lo retorna (`.pop()`)

Hay otra común que es ***peek*** que muestra el último elemeento sin sacarlo (`stack[-1]`). El _stack_ es una estructura de tipo **Last In, First Out** (LIFO)

## Colas (queues)

Estructura de datos secuancial que mantiene objetos ordenados según su orden de llegada, es de estructura ***First-in, First-out*** (FIFO).

Una cola tiene dos operaciones principales:

- ***Enqueue***: Agrega un elemento al final de la cola.
- ***Dequeue***: Saca el elemento que está al inicio de la cola. Esto siempre sacará el elemento que lleva más tiempo en la cola.

### Implementación en Python

El módulo `collections` no provee exactamente la estructura *queue*, sino que una versión con más operaciones llamada  *deque* (por *double ended queue*). Por ahora, nos limitaremos a indicar cómo implementar las operaciones de las colas con la clase `deque`, y en la siguiente sección profundizaremos en esta estructura.

| Operación                 | Código Python           | Descripción                                           |
|---------------------------|-------------------------|-------------------------------------------------------|
| Crear cola                | `cola = deque()`        | Crea una cola vacía                                   |
| Crear cola                | `cola = deque(lista)`   | Crea una cola a partir de los elementos de una lista  |
| *Enqueue*                 | `cola.append(elemento)` | Agrega un elemento al final de la cola                |
| *Dequeue*                 | `cola.popleft()`        | Retorna y extrae el elemento del principio de la cola |
| *Peek*                    | `cola[0]`               | Retorna el primer elemento de la cola sin extraerlo   |
| *length*                  | `len(cola)`             | Retorna la cantidad de elementos en la cola           |
|*is_empty*                 | `len(cola) == 0`        | Retorna true si la cola está vacía                    |

### Colas de doble extremo (*deque*)

Un *deque* (*double-ended queue*, lo pronunciamos "dec") es una estructura secuencial en la que es posible **agregar y sacar elementos desde ambos extremos en forma eficiente**, con un *costo constante por operación*. Esto quiere decir que, independientemente del largo de un *deque*, si éste tiene $N$ elementos, para agregar y sacar elementos siempre ejecutará *la misma* cantidad de operaciones. Esto es mucho mejor que si utilizamos una *lista*, en que la cantidad de operaciones depende de la cantidad de elementos en la lista. En Python, esta estructura es provista por la clase `deque` del módulo `collections`. Las principales operaciones que soporta son:

| Operación      | Código Python                | Descripción                                                      |
|----------------|------------------------------|------------------------------------------------------------------|
| Crear *deque*  | `deque()`                    | Crea un *deque* vacío                                            |
| Crear *deque*  | `deque(lista)`               | Crea un *deque* a partir de los elementos de una lista           |
| *Add first*    | `deque.appendleft(elemento)` | Agrega un elemento al inicio del *deque*                         |
| *Add last*     | `deque.append(elemento)`     | Agrega un elemento al final del *deque*                          |
| *Delete first* | `deque.popleft()`            | Retorna y extrae el primer elemento del *deque*                  |
| *Delete last*  | `deque.pop()`                | Retorna y extrae el último elemento del *deque*                  |
| *First*        | `deque[0]`                   | Retorna sin extraer el primer elemento del *deque*               |
| *Last*         | `deque[-1]`                  | Retorna sin extraer el último elemento del *deque*               |
| *length*       | `len(deque)`                 | Retorna el número de elementos en el *deque*                     |
| *Is empty*     | `len(deque) == 0`            | Retorna true si el *deque* está vacío                            |
| *Clear*        | `deque.clear()`              | Limpia el *deque*                                                |
| *Remove*       | `deque.remove(elemento)`     | Saca el primer elemento del *deque* que sea igual a `elemento`   |
| *Count*        | `deque.count(elemento)`      | Cuenta el número de elementos iguales a `elemento` en el *deque* |

Se puede concluir que un `deque` es una **generalización de los stacks y colas**

## Diccionarios

Es una estructura de datos no secuencial y **mutable** que permite asopciar pares de elementos mediante la relación **llave-valor**, se le consulta por una **llave** y retorna su **valor** asociado.

Los diccionarios están dados por la clase `dict`. Se escriben igual que una lista solo que con las llaves `{}`, y para asociar un valor a la llave se le coloca `:`, por ejemplo:

```python
monedas = {"Chile": "Peso", "Perú": "Soles", "España": "Euro",
           "Holanda": "Euro", "Brasil": "Real"}
```

y para obtener el valor que queremos, nombramos al diccionario y a la llave, `diccionario[llave]`

```python
moneda['Chile']
```

retornando `'Peso'`

Tambien podemos obtener el valor de la llave mediante el metodo `.get()` en el cual se le otorgan 2 parámetros, el primero es el nomrbe de la llave y el segundo un valor en el caso de que la llave **no exista**.}

Como son mutables, tienen dos compartamientos al asiganrle un valor a una llave, si la llave no existe se agrega al diccionario, en el caso de que exista tal llave, se actualiza su valor, y se lleva a cabo mediante `diccionario[llave] = valro`. Tambien se pueden eliminar llaves con su valor de los diccionarios mediante `del`, estilo: `del diccionario[llave]`

## Sets

Los _sets_ eliminan duplicados o revisa si un elemento se encuentra  se encuentra en esta estructura o no, y todo dee forma eficiente. Para crear un _set_ vacío se utiliza `set()` pero tambien se pueden crear no vacios utilizando `{}`

### Operaciones sobre los sets

| Operación | Código Python |
|-----------|---------------|
| Largo     | `len()`       |
| Añadir elementos | `.add()` |
| Sacar elemento | `.remove()` o `.discard()` (la diferencia es que .remove() tira error si no se encuentra el elemento en el set|
| Iterar | Con `for` es posible iterar un set, pero sin ningún orden en particular |

### Union e intersección de conjuntos

Se pueden unir dos conjuntos mediante el operador `|`, estilo tenemos un `set_a` y un `set_b`, para unirlos basta con `set_a | set_b`, tambien se puede utilizar el método `.union()` estilo `set_a.union(set_b)`, ambos no alteran los _sets_ originales.

Se puede encontrar la intersección entre 2 sets mediante el operador `&` o mediante el método `.intersection()`, y se utiliza igual q en la union.

### Diferencia y diferencia simétrica de conjuntos

Diferencia = `set_a - set_b` devuelve la parte de set_a que no coincide con b, o tambien `.difference()`

Diferencia simétrica = `set_a ^ set_b` devuelve las partes tanto de a como b que no coinciden, en un mismo set, tambien sirve `.synmetric_difference()`

## Args y Kwargs

Se pueden cololar tanto listas, tuplas como diccionarios en funciones que requieran mas de un parámetro, por ejemplo tenemos una función la cual requiere 3 parámetros y tengo una lista y/o tupla de largo 3 (o sea con 3 objetos), tan solo llamando a la funcion y colocando un * antes del nombre de la lista y/o tupla agarra todos los argumentos de forma posicional, `funcion(*lsita) | funcion(*tupla)`, en el caso de un diccionario se coloca `funcion(**diccionario)`

Resulta que es mediante el uso de `*` y `**` en la declaración de funciones que es posible establecer este comportamiento:

- `*args`: permite declarar una cantidad arbitraría de argumentos **posicionales**. Al llamarse la función, se reciben esos argumentos y son contenidos en una **tupla** accesible por `args`.
- `**kwargs`: permite declarar una cantidad arbitraría de argumentos **por palabra clave**. Al llamarse la función, se reciben esos argumentos y son contenidos en un **diccionario** accesible por `kwargs`.
