# Semana 0

1. [Path](#Path)
2. [Archivos (poco)](#Archivos)

## Path

Los path pueden ser **absolutos** o **relativos**.

El **absoluto** comienza desde la **raiz** del sistema de archivos, por ejemplo en Windows puede ser `\` o `C:\`, el problema es que requiere que la ruta exista **exactamente iugal** en todos los sistemas de archivos en que se ejecuta el programa.

El **relativo** comienza con el cracter de directorio raiz e indica una direcciónm **relativa a cierto directorio**. Por lo general se interpreta a partir de algún directorio específico, ( Ejemplo cuando se llama a un interprete de Python en un entorno virtual comienza con `env` que seria el entorno virtual metido en la carpeta y no con `C:\`).

Lo importante es que al usar **rutas absolutas** no importa desde que directorio se ejecuta el programa, en el ejemplo virtual, si no ejecuto en el entorno virtual con el interprete de Pyhon en el entorno virtual no econtraria el archivo, dado que el relativo **se realiza en cierto directorio** (o carpeta) del computador. EL contra de las rutas absolutas es que son específicas, en el caso de querer pasarle el código o programa a un tercero, no le correra dado que no tiene la misma _path_, por lo que con esta estructura única no se replica a otros computadores.

- El path se divide en dos partes:
  - El nombre del directorio o `dirname`, que es la carpeta donde se escuentra el archivo o directorio objetivo
  - El nombre del archivo o directorio objetivo, filename o `basename`, que es el nombre del archivo, incluyendo su extensión o directorio.

El módulo os.path permite visualizar y/o separar el path en `dirname` y `basename`

```python
import os

path1 = '/carpeta1/carpeta2/imagen.jpg'

dirname1 = os.path.dirname(path1)
basename1 = os.path.basename(path1)

print(f'path: {path1}')
print(f'dirname: {dirname1}')
print(f'basename: {basename1}')
```

Dando como resultado:

path: /carpeta1/carpeta2/imagen.jpg
dirname: /carpeta1/carpeta2
basename: imagen.jpg

El módulo `os.path` tambien permite separar la extención del archivo mediante el método `.splitext`:

```python
nombre_sin_extension, extension = os.path.splitext(basename1)
print(nombre_sin_extension)
print(extension)
```

Entregando:

imagen
.jpg

El método `os.path.join`, junta los argumentos dados con un el separador del sistema operativo donde se ejecute, con lo que se recomienda trabajar de esta forma **fuertemente**.

El método `os.listdir` entrega una lista con los nombres de directorios y archivos que se encuentran en ese directorio, en el caso de querer ver los contenidos almacenados en una carpeta dentro de un directorio, se debe poner el path o bien usar el método `.join`.

Ejemplo:

Tenemos la carpeta `data` que es el origen de nuestro directorio y dentro de esa carpeta tenmos la carptea `gato`, para poder ver la lista de contendios de la carpeta **gato** debemos correr el método `os.listdir` con el argumento con `.join`.

```python
contenidos_lista = os.listdir(os.path.join('data', 'gato'))
contenidos_lista
```

En cambio, el método `walk` nos permite poder obtener las rutas de un directorio, de sus subdirectorios y de sus archivos. Esto nos permite poder navegar dentro de una carpeta y ver, recursivamente, todo lo que contiene.

El siguiente código muestra como se utiliza:

```python
for raiz, directorios, archivos in os.walk("data", topdown = True):
    print("Raíz:",raiz)
    print()
    print("Archivos:")
    for archivo in archivos:
        print(os.path.join(raiz, archivo))
    print()
    print("Directorios:")
    for directorio in directorios:
        print(os.path.join(raiz, directorio))
    print("-"*30)
```

```python
'''
Raíz: data

Archivos:
data/archivo.txt
data/archivo_de_texto.jpg
data/files.png

Directorios:
data/gato
------------------------------
Raíz: data/gato

Archivos:
data/gato/juego_1.txt
data/gato/juego_2.txt

Directorios:
------------------------------
'''
```

El parámetro `topdown` nos permite decidir si la navegación sobre una carpeta será desde el directorio raíz (topdown = True) o desde sus elementos hojas (`topdown = False`).

## Archivos

### (poco)

abrir archivo: `open('archivo')`, y en el resto del argumento se le pude colocar `'rt'` que signifca abrir en modo lectura (`r`, _read_), y en forma texto (`t`), también esta el `'wt'`, que indica escribir (`w`, _write_) en forma texto (`t`)

Con el método `readlines` obtenemos uns lista de las lineas del archivo de texto

Recordatorio de listas = el `.strip()` tambien elimina los saltos de linea mencionados como `\n`

Siempre al manipular un archivo siempre hay que cerrarlo mediante el método `archivo.close()`, y existe una alternativa para el uso de `close`, que es abrir un archivo mediante la sentencia `with`.

Ejemplo:

```python
#En el primer argumento puede ir tanto el nombre del archivo como el path, todo depende en done se encuentre

with open('nombre_archivo', "rt") as archivo:
    lineas = archivo.readlines()
```

Como tambien se puede guardar el resultado o cualquier cosa en otro archivo mediante lo mismo.

```python
ruta_juego_2 = os.path.join("data", "gato", "juego_2.txt")

with open(ruta_juego_2, "wt") as archivo:
    for fila in tablero:
        fila_en_texto = ",".join(fila) + "\n"
        print(fila_en_texto)
        archivo.write(fila_en_texto)
```
