# Semana 5

## Iterables

**Iterable**: es cualquier **objeto sobre el cual se puede iterar**. Un *iterable* podría aparecer al lado derecho de un *for* (`for i in iterable:`). Estructuras *built-ins* como *sets*, listas, diccionarios y *deques*, son *iterables*.

**Iterador**: es un **objeto que itera sobre un iterable**, y es el objeto retornado por el método `__iter__()`. Este objeto iterador implementa el método `__next__()`, que nos retorna uno a uno los elementos de la estructura cada vez que se invoca a esta función. Cuando no quedan objetos por recorrer el iterador **debe** levantar una excepción de tipo `StopIteration`.

```python
## iter(conjunto) nos entrega un objeto que itera sobre ese conjunto
conjunto = {1, 3, 4, 6}
iterador = iter(conjunto)  # Esto es lo mismo que conjunto.__iter__()
print(type(iterador))

## Ahora vamos a invocar a next para que el iterador nos entregue el siguiente valor del iterable
print(next(iterador))      # Esto es lo mismo que iterador.__next__()
print(next(iterador))
print(next(iterador))
```

**Recordar**:
> Un iterable debe tener el método `__iter__` implementado, y debe retornar **siempre** un iterador. Por su parte, un iterador es un objeto que tiene el método `__next__` implementado, es decir puedo hacer `next(iterador)` y esto retornará un **valor**.

## Generadores

Los **generadores** son un caso especial de los **iteradores**. Los generadores nos permiten iterar sobre secuencias de datos sin la necesidad de almacenarlos en alguna estructura especial, evitando el uso innecesario de memoria.

Una vez que se termina de iterar sobre un generador, este desaparecee. La sintaxis para crear generadores es con `(` `)`.

```python
generador_pares = (2 * i for i in range(10)) # Por el sólo hecho de usar paréntesis estamos creando un generador.
```

### Funciones Generadoras

Las funciones en Python también tienen la posibilidad de funcionar como generadores, con la sentencia `yield`. El *statement* `yield` es un análogo a `return`, con ciertas diferencias. Por un lado, `yield` se encarga de retornar el valor indicado, pero también se asegura que en la próxima llamada a la función, la ejecución parta desde donde se dejó antes.

## Funciones _lambda_

**Las funciones *lambda*** son una forma alternativa de definir funciones en Python. Además de su nombre griego, no hay nada intimidante en ellas. Veamos un ejemplo de cómo definirlas:

```python
sucesor = lambda x: x + 1

# Es (casi) equivalente a
def sumar_uno(x):
    return x + 1


restar = lambda x, y: x - y

# Es (casi) equivalente a
def sustracción(x, y):
    return x - y
```

Como se puede observar, la sintaxis consiste en `lambda <parámetros>: <valor a retornar>`. En estas funciones no se necesita la sentencia `return`, puesto que la operación que se coloca a la derecha de los dos puntos (`:`) es el valor que se devolverá.

### `map`

`map` recibe como parámetros una función y **al menos** un iterable. Retorna un generador que resulta de aplicar la función sobre cada elemento del iterable. Es así como `map(f, iterable)` es equivalente a `(f(x) for x in iterable)`.

Notar que la cantidad de elementos que procesa la función en un `map` corresponde a la cantidad que tiene el iterable más pequeño.

## `filter`

`filter(f, iterable)` recibe como parámetros una función que retorna `True` o `False` (o función *booleana*), y un iterable. Retorna un generador que entrega aquellos elementos del iterable donde la función `f` retorna `True`.

Se puede ver que `filter(f, iterable)` es equivalente a `(x for x in iterable if f(x))`.

```python
set_filtrado = filter(lambda x: x < 10, {100, 1, 5, 9, 91, 1})
list(set_filtrado)
```

## `reduce`

Vamos a explicar la idea del `reduce` con un ejemplo de cálculo manual. Imaginemos que tenemos una secuencia con números, y que queremos obtener la suma de ellos. También supongamos que nos complica sumar más de dos números a la vez.

Esta operación consiste en aplicar sucesivamente una función `f(x, y)`, donde `x` es el resultado acumulado e `y` es un elemento de la secuencia. Esto *reducirá* el iterable a un sólo resultado. Entonces, `reduce(f, iterable)` recibe una función que toma dos valores y un iterable. Retorna lo que resulta de aplicar la función `f` al iterable `[s1, s2, s3, ..., sn]` de la siguiente forma: `f(f(f(f(s1, s2), s3), s4), s5), ...`.
