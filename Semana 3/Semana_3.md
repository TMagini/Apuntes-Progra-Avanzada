# Semana 3

## Multiherencia

Es precisamente tener mas de una clase asociada a una sub-clase, una cosa aprticular es la jerarquía diamante, que ocurre cuando una sub-clase depende de dos super-clases y estas dos a su vez dependen de una super-clase, en este caso cada sub clase es llama una única vez al realizar los métodos pero la clase raiz (o la primera clase, clase madre), es llamada dos veces.

Esta jeraquía siempre ocurre cuando hablamos de *Mulriherencia* dado que las dos super clases siempre dependen de una super clase madre que seria la clase ```object```, de esta heredan **todas** las clases que creamos. Por lo que siempre se llamará 2 veces a `object`.

### Solución

Aplicando el `super()`, en cada super-clase y tambien en la sub-clase, Python va a reccorer de **izquierda a derecha**, primero llamando a la izquierda, despues a la derecha y terminando en la super-clase madre, una vez cada uno.

### Orden de la herencia: método `__mro__`

EEste método muestra el orden de la jerarquía a partir de la clase actual, nos sirve para tema con multiherencia compleja. Si al momento de crear multihrencia no se sigue el orden, al crear la misma arroja error.

### Uso

Al usar el método `super().__init__()` (y asi evitarnos de que llame dos veces a la super-clase madre y asi MRO hace su trabajo) debemos entregar los argumentos para cada atributo, pero si le entregamos 2 argumentos de sus respectivas clases, este recibira un tercero, el `self`, por lo que nos lanza un error.

### Solución: uso de `*args` y `**kwargs`

* `**kwargs` es una *secuencia de argumentos de largo variable*, donde cada elemento de la lista tiene asociado un ***keyword***. El `**` mapea los elementos contenidos en el diccionario `kwargs` y los pasa a la función como _argumentos no posicionales_. Esto significa que los argumentos no se asignan a la función por su posición en el orden en que se entregan (como es lo habitual) sino por su _keyword_ asociado. De ahí el nombre _kwargs_ o _keyword arguments_. El `**kwargs` puede ser usado para enviar una cantidad variable de argumentos.
* `*args` es un mecanismo similar. `*args`, es una lista de argumentos de largo variable, pero sin *keywords* asociados. El operador `*` desempaqueta el contenido de args y los pasa a la función como argumentos posicionales. La función asigna valores a sus argumentos a partir del orden que trae esta lista.

El `**kwarg` recibe este diccionario y se va gastando cada vez que se le menciona en una super-clase. Ver ejemplo Semana 03.

## Clases abstractas

La sintaxis base de Python no tiene una forma de definir clases abstractas, pero si existe el módulo `abc` ("Abstract Base Classes") que nos provee herramientas para hacerlo. Mediante la clase `ABC` y el decorador `abstractmethod` es posible definir una clase abstracta.

La subclase `SubClase2` también es capaz de usar los métodos no abstractos de `Base`, pero re-implementa el método abstracto `metodo_2` accediendo a la definición original de `Base` mediante `super()`.
