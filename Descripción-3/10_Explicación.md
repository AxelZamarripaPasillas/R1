# 10_PROGRAMA QUE MUESTRA LA COMPARACIÓN DE ELEMENTOS EN LISTAS
Este programa muestra cómo se pueden comparar elementos en listas en Python utilizando los operadores "in" y "not in".

Línea 1: Esta línea crea una lista llamada "nombres" que contiene tres elementos: "Choto", "Emiliano" y "Luis". La lista se define utilizando corchetes `[]` y los elementos se separan 
con comas.

```python
nombres = ["Choto", "Emiliano", "Luis"]
```

Línea 2: Esta línea verifica si el elemento "Luis" se encuentra en la lista "nombres" utilizando el operador `in`. La comparación devuelve `True` porque el elemento "Luis" se encuentra en 
la lista.

```python
print ("Luis" in nombres)  # True
```

Línea 3: Esta línea verifica si el elemento "Emi" se encuentra en la lista "nombres" utilizando el operador `in`. La comparación devuelve `False` porque el elemento "Emi" no se encuentra 
en la  lista, aunque "Emiliano" sí.

```python
print ("Emi" in nombres)  # False
```

Línea 4: Esta línea verifica si el elemento "Javier" se encuentra en la lista "nombres" utilizando el operador `in`. La comparación devuelve `False` porque el elemento "Javier" no se 
encuentra en la lista.

```python
print ("Javier" in nombres)  # False
```

Línea 5: Esta línea verifica si el elemento "Jose" no se encuentra en la lista "nombres" utilizando el operador `not in`. La comparación devuelve True porque el elemento "Jose" no se 
encuentra en la lista.

```python
print ("Jose" not in nombres)  # True
```
