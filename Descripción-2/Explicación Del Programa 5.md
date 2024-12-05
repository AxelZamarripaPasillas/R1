# PROGRAMA 5 DE COMPARACIONES CON "STRING"
Programa que demuestra el uso de operadores de comparación, `membresía` y `slicing` en Python.
## Explicación Del Programa:

### COMPARACIONES:

Línea 6: Esta línea utiliza el operador `==` para comparar si las cadenas de texto "perro" y "perro" son iguales. El resultado es `True` porque las cadenas son idénticas.

```python
print ("perro" == "perro") # True
```

Línea 7: Esta línea utiliza el operador `!=` para comparar si las cadenas de texto "perro" y "gato" son diferentes. El resultado es `True` porque las cadenas son diferentes.

```python
print ("perro" != "gato") # True
```

Línea 8: Esta línea utiliza el operador `<` para comparar si la cadena de texto "Aguascalientes" es menor que la cadena de texto "Zacatecas". El resultado es `False` porque la cadena "Aguascalientes" es mayor que la cadena "Zacatecas" en orden alfabético.

```python
print ("Aguascalientes" < "Zacatecas") # False
```

Línea 9: Esta línea utiliza el operador `>=` para comparar si la cadena de texto "Aire" es mayor o igual que la cadena de texto "Agua". El resultado no se muestra en el código, pero sería `True` porque la cadena "Aire" es mayor que la cadena "Agua" en orden alfabético.

```python
print ("Aire" >= "Agua") # True
```

## MEMBERSHIP:
Línea 14: Esta línea utiliza el operador `in` para verificar si la cadena de texto "house" se encuentra dentro de la cadena de texto "boathouse". El resultado es `True` porque la cadena "house" es una subcadena de la cadena "boathouse".

```python
print ("house" in "boathouse") #True
```

Línea 15: Esta línea utiliza el operador `in` para verificar si la cadena de texto "bien" se encuentra dentro de la cadena de texto "bienvenidos". El resultado es `True` porque la cadena "bien" es una subcadena de la cadena "bienvenidos".

```python
print ("bien" in "bienvenidos") #True
```

Línea 16: Esta línea utiliza el operador `not in` para verificar si la cadena de texto "y" no se encuentra dentro de la cadena de texto "ejes". El resultado es `True` porque la cadena "y" no es una subcadena de la cadena "ejes".

```python
print ("y" not in "ejes") #True
```

Línea 17:  Esta línea utiliza el operador `not in` para verificar si la cadena de texto "je" no se encuentra dentro de la cadena de texto "ejes". El resultado es `False` porque la cadena "je" es una subcadena de la cadena "ejes".

```python
print ("je" not in "ejes") #False
```

### SLICING (REBANADOR):
Línea 21: Esta línea asigna la cadena de texto "Choto Chorchis" a la variable "mi_nombre".

```python
mi_nombre = "Choto Chorchis"
```

Línea 22: Esta línea utiliza el índice 3 para acceder al cuarto carácter de la cadena de texto "mi_nombre". El resultado es el carácter "t".

```python
print (mi_nombre [3])
```

Línea 23: Esta línea utiliza el índice 12 para acceder al decimotercer carácter de la cadena de texto "mi_nombre". El resultado es el carácter "s".

```python
print (mi_nombre [12])
```

Línea 26: Esta línea asigna la cadena de texto "JOSÉ LUIS" a la variable "mi_nombre".

```python
mi_nombre = "JOSÉ LUIS"
```

Línea 27: Esta línea utiliza el índice `2:6` para acceder a los caracteres desde el tercer carácter hasta el sexto carácter de la cadena de texto "mi_nombre". El resultado es la cadena de texto "SÉ L".

```python
print (mi_nombre [2:6])
```

