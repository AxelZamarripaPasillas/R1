# PROGRAMA 10 QUE PERMITE REVISAR SI PUEDES VER UNA PELÍCULA EN NETFLIX
Programa que determina si un usuario puede ver una película en Netflix según su edad y si ha comprado la película.
## Explicación Del Programa:
Este programa solicita al usuario que ingrese su edad y si ha comprado la película. Luego, utiliza una expresión lógica para determinar si el usuario puede ver la película.
### Solución 1. If Anidados

Línea 6: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese su edad. La función `int()` se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable edad.

```python
edad = int(input("¿Cuántos Años Tienes"))
```

Línea 7: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese si compró la película o no. La función `int()` se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable comprar.

```python
comprar= int(input("¿Compraste La Película? \n0-NO\n1-SI\n"))
```

Línea 9: Esta línea utiliza la sentencia condicional `if` para verificar si la edad del usuario es mayor o igual a 18. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del `bloque if`.

```python
if edad >=18:
```

Línea 10: Esta línea utiliza la sentencia condicional `if` para verificar si el usuario compró la película. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del `bloque if`.

```python
if comprar == 1:
```

Línea 11: Esta línea se ejecuta si las condiciones `edad >=18` y `comprar == 1` son verdaderas. Imprime el mensaje "Puede Ver La Película" en la pantalla.

```python
print("Puede Ver La Película")
```

Línea 13: Esta línea se ejecuta si la condición `comprar == 1` es falsa. Imprime el mensaje "Vete a Hacer La Tarea" en la pantalla.

```python
else: print("Vete a Hacer La Tarea")
```

Línea 11: Esta línea imprime un mensaje de agradecimiento en la pantalla.

```python
print("¡Gracias Por Usar Netflix!")
```

### Solución 2. Con Compuertas.

Línea 20: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese su edad. La función `int()` se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable edad.

```python
edad = int(input("¿Cuántos Años Tienes? "))
```

Línea 21: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese si compró la película o no.

```python
comprar = input ("¿Compraste La Película? \n0-NO\n1-SI\n")
```

Línea 23: Esta línea utiliza la sentencia lógica `and` para verificar si la edad del usuario es mayor o igual a 18 y si compró la película. El resultado se asigna a la variable `puede_ver_pelicula`.

```python
puede_ver_pelicula = edad >=18 and comprar
```

Línea 25: Esta línea utiliza la sentencia condicional `if` para verificar si la variable `puede_ver_pelicula` es verdadera. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del `bloque if`.

```python
if puede_ver_pelicula:
```

Línea 25: Esta línea se ejecuta si la condición `puede_ver_pelicula` es verdadera. Imprime el mensaje "Puedes Ver La Película" en la pantalla.

```python
print ("Puedes Ver La Película")
```

Línea 26: Esta línea se ejecuta si la condición `puede_ver_pelicula` es falsa. Imprime el mensaje "No Puedes Ver La Película" en la pantalla.

```python
else: print ("No Puedes Ver La Película")
```

Línea 28: Esta línea imprime un mensaje de agradecimiento en la pantalla.

```python
print ("¡Garcias Por Usar Netflix!")
```

