# 8_PROGRAMA QUE MUESTRA EJEMPLOS DE INDEXING Y SUBSCRIPTING EN LISTAS
Este programa muestra ejemplos de cómo acceder a elementos individuales en listas utilizando indexing y subscripting.

Línea 1: Esta línea imprime un título que indica que se van a mostrar ejemplos de indexing.

```python
print ("-----INDEXING")
```

Línea 2: Esta línea crea una lista llamada `numero` que contiene tres elementos: 10, 20 y 30.

```python
numero = [10, 20, 30]
```

Línea 3: Esta línea imprime el tercer elemento de la lista `numero` utilizando el índice 2. En Python, los índices comienzan en 0, por lo que el tercer elemento tiene un índice 
de 2.

```python
print (numero[2])
```

Línea 4: Esta línea imprime el primer elemento de la lista `numero` utilizando el índice 0.

```python
print (numero[0])
```

Línea 5: Esta línea imprime el segundo elemento de la lista `numero` utilizando el índice 1.

```python
print (numero[1])
```

Línea 6: Esta línea imprime el último elemento de la lista `numero` utilizando el índice -1. En Python, los índices negativos se utilizan para acceder a los elementos de la 
lista en orden inverso.

```python
print (numero[-1])
```

Línea 7: Esta línea imprime un título que indica que se van a mostrar ejemplos de subscripting.

```python
print ("\n-----SUBSCRIPTING")
```

Línea 8: Esta línea crea una lista llamada `nombre` que contiene cuatro elementos: "Chorchis", "Choto", "Emiliano" y "Pepe".

```python
nombre = ["Chorchis", "Choto", "Emiliano", "Pepe"]
```

Línea 9: Esta línea imprime todos los elementos de la lista `nombre` a partir del segundo elemento (índice 1) utilizando la sintaxis de subscripting `[1:]`. 
El signo de dos puntos `(:)` indica que se deben incluir todos los elementos a partir del índice especificado.

```python
print (nombre [1:])
```

Línea 10: Esta línea imprime los elementos de la lista `nombre` del segundo al quinto elemento (índices 1 a 4) utilizando la sintaxis de subscripting `[1:5]`.
El signo de dos puntos `(:)` indica que se deben incluir todos los elementos entre los índices especificados.

```python
print (nombre [1:5])
```

Línea 11: Esta línea imprime los dos últimos elementos de la lista `nombre` utilizando la sintaxis de subscripting `[-2:]`. El signo de dos puntos `(:)` indica 
que se deben incluir todos los elementos a partir del índice especificado.

```python
print (nombre [-2:])
```
