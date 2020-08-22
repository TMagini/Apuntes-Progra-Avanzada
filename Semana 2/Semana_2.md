# Semana 2

1. [Objetos](#Objetos)
2. [Properties: `property`](#Properties)

## Objetos

### Encapsulamiento

El caracter _underscore_ `_` permite otorgar un atributo o método que se utilizara solo en el código de la clase, dado que los atributos que no lleven este caracter podran ser utilizados de manera *Pública*, y los q tengan el `_` solo sern utilizados de manera *Privada*

A pesar de esto, aun asi podemos llamar a los métodos con `_` ( aunq no deberia ), pero si realmente queremos que los métodos o atributos sean secretos hacemos un _dobleunderscore_ `__` y si llamamos a los métodos o atributos de la manera tradicional, Python dira que no existen ( a persar de que si), aun asi podemos llamar a estos métodos si los mensionamos de esta manera `_NombreDeLaClase__atributo_o_metodo_secreto` (Este truco se conoce como _name mangling_)

## Properties

Funciona como un atributo en el cual podemos modificar su comportamiento cada vez que es leído (`get`), escrito (`set`), o eliminado (`del`). Al utilizar _properties_ sobre un atributo, las accioneas a ejecutar se realzian de manera más limpia que invocando métodos explícitos. Tambien podemos utilizar los métodos _getter_ y _setter_.

_Setter_ :

```python
## Método setter
    def set_kilometraje(kms):
        self.__kilometraje = kms
```

_Getteer_:

```python
    ## Método getter
    def get_kilometraje():
        return self.__kilometraje
```

La gracia de ocupar `properties` es que podemos modificar un atributo privado de manera más sencilla, por ejemplo:

```python
class Puente:

    def __init__(self, maximo):
        self.maximo = maximo
        self.__personas = 0

    @property
    def personas(self):
        return self.__personas

    @personas.setter
    def personas(self, p):
        if p > self.maximo:
            self.__personas = self.maximo
        elif p < 0:
            self.__personas = 0
        else:
            self.__personas = p
```

El `@` es el *decorador*, si no lee ponemos nada a la propertie esta se comporta como un atributo, cuyo mettodo es el _getter_, despues podemos ver el _setter_ que nos permite modificar el valor de la _property_

Otra forma de escribirlo puede ser:

```python
class Puente:

    def __init__(self, maximo):
        self.maximo = maximo
        self.__personas = 0

    def _get_personas(self):
        return self.__personas

    def _set_personas(self, p):
        if p > self.maximo:
            self.__personas = self.maximo
        elif p < 0:
            self.__personas = 0
        else:
            self.__personas = p

    personas = property(_get_personas, _set_personas)
```

## Herencia

Como vien dice el nombre, es cuando una clase "hereda", los métodos y atributos de otra clase, hablando mas formal, es cuando tenemos una super clase (la clase principal de la cual se heredan las cosas) y una subclase que es la q hereda todo. Un ejemplo:

```python
class Auto:

    def __init__(self, ma, mo, a, c, k):
        self.marca = ma
        self.modelo = mo
        self.año = a
        self.color = c
        self.__kilometraje = k
        self.__dueño = None

    def conducir(self, kms):
        print(f"Conduciendo {kms} kilómetros")
        self.__kilometraje += kms

    def vender(self, nuevo_dueño):
        self.__dueño = nuevo_dueño
        print(f"Auto vendido a {nuevo_dueño}")

    def leer_odometro(self):
        return self.__kilometraje


class FurgónEscolar(Auto): # Aquí se marca de donde hereda
    """Subclase de Auto"""

    def __init__(self, marca, modelo, año, color, kms):
        # Para inicializar algunos datos en la clase madre, llamamos explícitamente
        # al __init__ de esa clase.
        Auto.__init__(self, marca, modelo, año, color, kms)
        # Este atributo existe únicamente para objetos de tipo FurgonEscolar,
        # pero no para todos los objetos de clase Auto
        self.niños_y_niñas = []

    # inscribir_niño_o_niña es un método específico de esta subclase.
    def inscribir_niño_o_niña(self, niño_o_niña):
        self.niños_y_niñas.append(niño_o_niña)

```

### Overriding

También podemos modificar métodos de la super clase dado que no siempre nos van a servir, y para poder hacer esto simplemente cuando definimos la sub-clase, volvemos a definir el método que existe en la super-clase
