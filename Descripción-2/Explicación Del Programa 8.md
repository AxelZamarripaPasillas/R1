## PROGRAMA DE CONDICIONAL IF
En este programa, se muestra cómo utilizar la sentencia condicional if para tomar decisiones basadas en una condición. En este caso, se calcula el promedio final de una serie de calificaciones y se determina si el estudiante aprobó o reprobó. Este programa solicita al usuario que ingrese las calificaciones de 6 unidades, calcula el promedio final y determina si el estudiante aprobó o reprobó.

### Explicación Del Programa:
#### Línea 5: 
calificacion_1 = float(input("Ingresa La Calificación De La Unidad 1: "))

Esta línea utiliza la función input para solicitar al usuario que ingrese la calificación de la unidad 1. La función float se utiliza para convertir la entrada del usuario en un número flotante. El resultado se asigna a la variable calificacion_1.

Se repiten las mismas instrucciones para las unidades 2 a 6.

#### Línea 12: 
calificacion_final = (calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5 + calificacion_6)/6

Esta línea calcula el promedio final de las calificaciones ingresadas. Se suma el valor de cada variable calificacion_ y se divide por 6.

#### Línea 14: 
print ("Tu Promedio Final Es: ", calificacion_final)

Esta línea imprime el promedio final calculado en la línea anterior.

#### Línea 16: 
if calificacion_final >= 70:

Esta línea utiliza la sentencia condicional if para verificar si el promedio final es mayor o igual a 70. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque if.

#### Línea 17:
print ("Aprobaste")

Esta línea se ejecuta si la condición calificacion_final >= 70 es verdadera. Imprime el mensaje "Aprobaste" en la pantalla.

#### Línea 19: 
else:

Esta línea utiliza la sentencia else para especificar el código que se ejecutará si la condición calificacion_final >= 70 es falsa.

#### Línea 20: 
print ("Reprobaste")

Esta línea se ejecuta si la condición calificacion_final >= 70 es falsa. Imprime el mensaje "Reprobaste" en la pantalla.



