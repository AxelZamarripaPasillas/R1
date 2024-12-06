# 1_PROGRAMA QUE DETERMINA EL TIPO DE MASCOTA
Este programa solicita al usuario que ingrese el tipo de mascota que tiene y luego imprime un mensaje indicando si la mascota es un perro, un gato o un tipo de mascota desconocido.

## Explicación Del Programa: 
Línea 1: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese el tipo de mascota que tiene. La entrada del usuario se almacena en la variable `mascota`.

```python
mascota = input("Ingresa El Tipo De Mascota Que Tienes: ")
```

Línea 3: Esta línea utiliza una estructura de control condicional `if` para verificar si la palabra "perro" está dentro de la variable `mascota`.

```python
if "perro" in mascota:
```

Línea 4-5: Esta línea utiliza una estructura de control condicional `elif` para verificar si la palabra "gato" está dentro de la variable `mascota`.

```python
print("Es Un Perro")
```

Línea 6-7: Esta línea utiliza una estructura de control condicional `else` para imprimir un mensaje indicando que el tipo de mascota es desconocido si ninguna de las condiciones anteriores se cumple.

```python
elif "gato" in mascota:
    print("Tienes Un Gato ")
```

Línea 9-10: Esta línea utiliza una estructura de control condicional `else` para imprimir un mensaje indicando que el tipo de mascota es desconocido si ninguna de las condiciones anteriores se cumple.

```python
else:
    print("Tipo De Mascota Desconocida")
```

Línea 11: Esta línea imprime un mensaje de agradecimiento al usuario por utilizar el programa utilizando la función `print()`.

```python
print("¡Gracias Por Usar Nuestro Programa! ")
```

