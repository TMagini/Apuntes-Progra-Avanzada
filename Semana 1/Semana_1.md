# Semana 1 | Estructuras de datos

1. [Tuplas](#Tuplas)
2. [Listas (super poco)](#Listas)

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
