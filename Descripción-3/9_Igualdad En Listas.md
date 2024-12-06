# 9_PROGRAMA QUE MUESTRA LA COMPARACIÓN DE LISTAS EN PYTHON
Este programa muestra cómo se pueden comparar listas en Python utilizando los operadores de igualdad y desigualdad.

Línea 1: Esta línea crea una lista llamada `puntos` que contiene tres elementos: 10, 30 y 20. La lista se define utilizando corchetes `[]` y los elementos se separan con comas.

```python
puntos = [10, 30, 20]
```

Línea 2: Esta línea crea una lista llamada `puntos_2` que es idéntica a la lista `puntos`. La lista se define de la misma manera que la lista `puntos`.


```python
puntos_2 = [10, 30, 20]
```

Línea 3: Esta línea crea una lista llamada `ordenados` que contiene los mismos elementos que la lista `puntos` pero en orden ascendente. La lista se define de la misma 
manera que las listas 
anteriores.

```python
ordenados = [10, 20, 30]
```

Línea 4: Esta línea crea una lista llamada `puntos_texto` que contiene los mismos elementos que la lista `puntos` pero como cadenas de texto. La lista se define de la misma 
manera que las listas anteriores.

```python
puntos_texto = ["10", "20", "30"]
```

Línea 5: Esta línea compara la lista `puntos` con la lista `puntos_2` utilizando el operador de igualdad `(==)`. La comparación devuelve True porque las listas son idénticas.

```python
print (puntos == puntos_2)  # True
```

Línea 6: Esta línea compara la lista `puntos` con la lista `ordenados` utilizando el operador de igualdad `(==)`. La comparación devuelve False porque las listas tienen los 
mismos elementos pero en orden diferente.

```python
print (puntos == ordenados)  # False
```

Línea 7
Esta línea compara la lista `puntos` con ella misma utilizando el operador de igualdad `(==)`. La comparación siempre devuelve `True`.

```python
print (puntos == puntos)  # True
```

Línea 8
Esta línea compara la lista `puntos` con la lista `puntos_2` utilizando el operador de desigualdad `(!=)`. La comparación devuelve False porque las listas son idénticas.

```python
print (puntos != puntos_2)  # False
```

Línea 9
Esta línea compara la lista `puntos` con la lista `ordenados` utilizando el operador de desigualdad `(!=)`. La comparación devuelve True porque las listas tienen los mismos 
elementos pero en orden diferente.

```python
print (puntos != ordenados)  # True
```

Línea 10
Esta línea compara la lista `puntos` con ella misma utilizando el operador de desigualdad `(!=)`. La comparación siempre devuelve `False`.

```python
print (puntos != puntos)  # False
```
