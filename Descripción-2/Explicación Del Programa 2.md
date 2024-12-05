# PROGRAMA 2 PARA PROBAR LAS COMPUERTAS LÓGICAS AND, OR y NOT
Programa que demuestra el funcionamiento de la operación lógica OR y la negación (NOT) en Python.

### Explicación Del Programa:
Este programa muestra cómo funciona la operación lógica OR y la negación (NOT) en Python. La operación OR devuelve `True` si al menos uno de los operandos es `True`. La negación (NOT) invierte el valor lógico de su operando.

Línea 6: Esta línea utiliza la función `print○` para mostrar el resultado de la operación lógica `OR` entre `False y False`. La función `OR` devuelve `True` si alguno de los operandos es `True`, y `False` en caso contrario. En este caso, ambos operandos son `False`, por lo que el resultado es `False`.

```python
print (False or False) #False
```

Línea 7: Esta línea utiliza la función print para mostrar el resultado de la operación lógica OR entre False y True. La función OR devuelve True si alguno de los operandos es True, y False en caso contrario. En este caso, uno de los operandos es True, por lo que el resultado es True.

```python
print (False or True) #True
```

Línea 8: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `OR` entre `True y False`. La función `OR` devuelve `True` si alguno de los operandos es `True`, y `False` en caso contrario. En este caso, uno de los operandos es `True`, por lo que el resultado es `True`.

```python
print (True or False) #True
```

Línea 9: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `OR` entre `True` y `True`. La función `OR` devuelve `True` si alguno de los operandos es `True`, y `False` en caso contrario. En este caso, ambos operandos son `True`, por lo que el resultado es `True`.

```python
print (True or True) #True
```

Línea 14: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `NOT` aplicada a la expresión `False or False`. La función `NOT` devuelve el opuesto lógico de la expresión. En este caso, la expresión `False or False` es `False`, por lo que el resultado de la función `NOT` es `True`.

```python
print (not(False or False)) # True
```

Línea 15: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `NOT` aplicada a la expresión `False or True`. La función `NOT` devuelve el opuesto lógico de la expresión. En este caso, la expresión `False or True` es `True`, por lo que el resultado de la función `NOT` es `False`.

```python
print (not(False or True)) # False
```

Línea 16: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `NOT` aplicada a la expresión `True or False`. La función `NOT` devuelve el opuesto lógico de la expresión. En este caso, la expresión `True or False` es `True`, por lo que el resultado de la función `NOT` es `False`.

```python
print (not(True or False)) # False
```

Línea 17: Esta línea utiliza la función `print` para mostrar el resultado de la operación lógica `NOT` aplicada a la expresión `True or True`. La función `NOT` devuelve el opuesto lógico de la expresión. En este caso, la expresión `True or True` es `True`, por lo que el resultado de la función `NOT` es `False`.

```python
print (not(True or True)) # False
```

