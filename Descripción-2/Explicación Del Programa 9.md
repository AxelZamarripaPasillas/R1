# PROGRAMA 9 DE CONDICIONAL IF
Programa que calcula el total a pagar por una cantidad de artículos comprados, aplicando un descuento si la cantidad es mayor a 3.
## Explicación Del Programa:
Este programa solicita al usuario que ingrese la cantidad de artículos comprados y calcula el total a pagar según la siguiente lógica:

- Si la cantidad de artículos es mayor a 3, el precio por artículo es de $30.
- Si la cantidad de artículos es 3 o menos, el precio por artículo es de $45.

Línea 4: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese la cantidad de artículos comprados. La función `int()` se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable cantidad.

```python
cantidad = int (input("¿Cuántos Artículos Compró?"))
```

Línea 6: Esta línea utiliza la sentencia condicional `if` para verificar si la cantidad de artículos comprados es mayor que 3. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del `bloque if`.

```python
if cantidad >3:
```

Línea 7:  Esta línea se ejecuta si la condición `cantidad >3` es verdadera. Calcula el total a pagar multiplicando la cantidad de artículos comprados por 30.

```python
total= cantidad * 30
```

Línea 8: Esta línea utiliza la sentencia `else` para especificar el código que se ejecutará si la condición `cantidad >3` es falsa.

```python
else:
```

Línea 9: Esta línea se ejecuta si la condición `cantidad >3` es falsa. Calcula el total a pagar multiplicando la cantidad de artículos comprados por 45.

```python
total = cantidad * 45
```

Línea 10: Esta línea imprime el total a pagar calculado en las líneas anteriores. La función `str()` se utiliza para convertir el valor de total en una cadena de texto.

```python
print ("El Total a Pagar Es $" + str(total))
```
Línea 11: Esta línea imprime un mensaje de saludo en la pantalla.

```python
print("Saludo...")
```



