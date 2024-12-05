# 1_PROGRAMA QUE MUESTRA LA COMPUERTA NOT
Programa que demuestra el funcionamiento de la compuerta lógica NOT en Python.

## Explicación Del Programa:
Este programa muestra cómo funciona la compuerta lógica NOT en Python. La compuerta NOT es una operación lógica que invierte el valor de un booleano.

Línea 6: Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión `True`. La función `not` se utiliza para negar la expresión `True`, lo que resulta en `False`.

```python
print (not True) # Imprime False
```

Línea 7:  Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión "False". La función `not` se utiliza para negar la expresión "False", lo que resulta en "True".

```python
print (not False) # Imprime True
```

Línea 11:  Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión "False or False". La función `not` se utiliza para negar la expresión "False or False", lo que resulta en "True".

```python
print (not(False or False)) # True
```

Línea 12: Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión "False or True". La función `not` se utiliza para negar la expresión "False or True", lo que resulta en "False".

```python
print (not(False or True)) # False
```

Línea 13: Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión "True or False". La función `not` se utiliza para negar la expresión "True or False", lo que resulta en "False".

```python
print (not(True or False)) # False
```

Línea 14: Esta línea utiliza la función `print()` para mostrar el resultado de la negación de la expresión "True or True". La función `not` se utiliza para negar la expresión "True or True", lo que resulta en "False".

```python
print (not(True or True)) # False
```

