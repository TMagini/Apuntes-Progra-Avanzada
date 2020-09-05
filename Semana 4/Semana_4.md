# Semana 4

## Levantamiento y manejo de excepciones

### Levantamiento

Podemos generar una excepción en el momento que queramos creando una nueva instancia de la excepción, y utilizando la sentencia **`raise`**. Cada excepción tiene un tipo definido, y es posible definir un mensaje explicativo para el usuario.

### Manejo: `try` y `except

Múltiples excepciones con `except`:

```python
# En esta parte manejamos las excepciones una vez que son lanzadas
except TypeError as error:
    # Este bloque sólo maneja excepciones del tipo TypeError
    print(f"Error: {error}")
    print("Revise el tipo del argumento.")

except ValueError as error:
    # Este bloque sólo maneja excepciones del tipo ValueError
    print(f"Error: {error}")
    print("Se produjo un ValueError. Verifique sus valores.")
```

### Flujos complementarios: `else` y `finally`

- Las instrucciones dentro del bloque `else` se ejecutarán **siempre y cuando no se haya lanzado ninguna excepción**.
- En el bloque de la sentencia `finally` van instrucciones que se realizan **siempre, independientemente de si ocurrió una excepción o no**.

## Utilizar el `except`

Si bien es posible manejar cualquier tipo de excepción capturando `Exception`, esto se considera una mala práctica, pues capturar una excepción sin saber su naturaleza, puede causar comportamientos inesperados en el programa.

Revisar archivo semana 4 para ver ejemplos.
