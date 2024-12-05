# PROGRAMA DE CONDICIONAL IF
Programa que calcula el promedio final de un estudiante en base a las calificaciones de 6 unidades y determina si aprobó o reprobó.
## Explicación Del Programa:
Este programa solicita al usuario que ingrese las calificaciones de 6 unidades, calcula el promedio final y determina si el estudiante aprobó o reprobó según un umbral de 70 puntos.

Línea 5: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese la calificación de la unidad 1. La función `float()` se utiliza para convertir la entrada del usuario en un número flotante. El resultado se asigna a la variable "calificacion_1".

```python
calificacion_1 = float(input("Ingresa La Calificación De La Unidad 1: "))
```

Se repiten las mismas instrucciones para las unidades 2 a 6.

```python
calificacion_2 = float(input("Ingresa La Calificación De La Unidad 2: "))
calificacion_3 = float(input("Ingresa La Calificación De La Unidad 3: "))
calificacion_4 = float(input("Ingresa La Calificación De La Unidad 4: "))
calificacion_5 = float(input("Ingresa La Calificación De La Unidad 5: "))
calificacion_6 = float(input("Ingresa La Calificación De La Unidad 6: "))
```

Línea 12:  Esta línea calcula el promedio final de las calificaciones ingresadas. Se suma el valor de cada variable calificacion_ y se divide por 6.

```python
calificacion_final = (calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5 + calificacion_6)/6
```

Línea 14: Esta línea imprime el promedio final calculado en la línea anterior.

```python
print ("Tu Promedio Final Es: ", calificacion_final)
```

Línea 16: Esta línea utiliza la sentencia condicional `if` para verificar si el promedio final es mayor o igual a 70. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del `bloque if`.

```python
if calificacion_final >= 70:
```

Línea 17: Esta línea se ejecuta si la condición calificacion_final `>= 70 es verdadera. Imprime el mensaje "Aprobaste" en la pantalla.

```python
print ("Aprobaste")
```

Línea 19: Esta línea utiliza la sentencia `else` para especificar el código que se ejecutará si la condición `calificacion_final >= 70` es falsa.

```python
else:
```

Línea 20: Esta línea se ejecuta si la condición `calificacion_final >= 70` es falsa. Imprime el mensaje "Reprobaste" en la pantalla.

```python
print ("Reprobaste")
```




