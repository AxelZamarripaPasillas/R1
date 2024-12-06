# 1_PROGRAMA QUE DETERMINA EL TIPO DE MASCOTA
Este programa solicita al usuario que ingrese el tipo de mascota que tiene y luego imprime un mensaje indicando si la mascota es un perro, un gato o un tipo de mascota desconocido.

Línea 1: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese el tipo de mascota que tiene. La entrada del usuario se almacena en la variable `mascota`.
La función `input()` devuelve una cadena de texto que es almacenada en la variable `mascota`.

```python
mascota = input("Ingresa El Tipo De Mascota Que Tienes: ")
```

Línea 3: Esta línea utiliza una estructura de control condicional `if` para verificar si la palabra "perro" está dentro de la variable `mascota`. La estructura de control condicional `if` es una instrucción que permite ejecutar un bloque de código si se cumple una condición. En este caso, se utiliza para verificar si la palabra "perro" está dentro de la variable `mascota`. Si la condición se cumple, se ejecuta el bloque de código que sigue a la instrucción `if`.

```python
if "perro" in mascota:
```

Línea 4-5: Esta línea imprime un mensaje indicando que es un perro si la condición se cumple. La función `print()` es una función incorporada en Python que permite imprimir mensajes en la pantalla. En este caso, se utiliza para imprimir un mensaje indicando que es un perro si la condición se cumple.

```python
print("Es Un Perro")
```

Línea 6-7: Esta línea utiliza una estructura de control condicional `elif` para verificar si la palabra "gato" está dentro de la variable `mascota`. La estructura de control condicional `elif` es una instrucción que permite ejecutar un bloque de código si se cumple una condición. En este caso, se utiliza para verificar si la palabra "gato" está dentro de la variable `mascota`. Si la condición se cumple, se ejecuta el bloque de código que sigue a la instrucción `elif`.

```python
elif "gato" in mascota:
    print("Tienes Un Gato ")
```

Línea 9-10: Esta línea utiliza una estructura de control condicional `else` para imprimir un mensaje indicando que el tipo de mascota es desconocido si ninguna de las condiciones anteriores se cumple. La estructura de control condicional `else` es una instrucción que permite ejecutar un bloque de código si ninguna de las condiciones anteriores se cumple. En este caso, se utiliza para imprimir un mensaje indicando que el tipo de mascota es desconocido si ninguna de las condiciones anteriores se cumple.

```python
else:
    print("Tipo De Mascota Desconocida")
```

Línea 11: Esta línea imprime un mensaje de agradecimiento al usuario por utilizar el programa utilizando la función `print()`. La función `print()` es una función incorporada en Python que permite imprimir mensajes en la pantalla. En este caso, se utiliza para imprimir un mensaje de agradecimiento al usuario por utilizar el programa.

```python
print("¡Gracias Por Usar Nuestro Programa! ")
```

