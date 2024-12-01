## PROGRAMA QUE PERMITE REVISAR SI PUEDES VER UNA PELÍCULA EN NETFLIX
En este programa, se muestra cómo utilizar sentencias condicionales y lógicas para determinar si un usuario puede ver una película en Netflix. Este programa solicita al usuario que ingrese su edad y si compró la película, y determina si puede ver la película en Netflix.
### Explicación Del Programa:
#### Solución 1. If Anidados

##### Línea 6: 
edad = int(input("¿Cuántos Años Tienes"))

Esta línea utiliza la función input para solicitar al usuario que ingrese su edad. La función int se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable edad.

#### Línea 7: 
comprar= int(input("¿Compraste La Película? \n0-NO\n1-SI\n"))

Esta línea utiliza la función input para solicitar al usuario que ingrese si compró la película o no. La función int se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable comprar.

#### Línea 9: 
if edad >=18:

Esta línea utiliza la sentencia condicional if para verificar si la edad del usuario es mayor o igual a 18. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque if.

#### Línea 10: 
if comprar == 1:

Esta línea utiliza la sentencia condicional if para verificar si el usuario compró la película. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque if.

#### Línea 11: 
print("Puede Ver La Película")

Esta línea se ejecuta si las condiciones edad >=18 y comprar == 1 son verdaderas. Imprime el mensaje "Puede Ver La Película" en la pantalla.

#### Línea 13: 
else: print("Vete a Hacer La Tarea")

Esta línea se ejecuta si la condición comprar == 1 es falsa. Imprime el mensaje "Vete a Hacer La Tarea" en la pantalla.

#### Línea 11: 
print("¡Gracias Por Usar Netflix!")

Esta línea imprime un mensaje de agradecimiento en la pantalla.

#### Solución 2. Con Compuertas.

#### Línea 20: 
edad = int(input("¿Cuántos Años Tienes? "))

Esta línea utiliza la función input para solicitar al usuario que ingrese su edad. La función int se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable edad.

#### Línea 21: 
comprar = input ("¿Compraste La Película? \n0-NO\n1-SI\n")

Esta línea utiliza la función input para solicitar al usuario que ingrese si compró la película o no.

#### Línea 23: 
puede_ver_pelicula = edad >=18 and comprar

Esta línea utiliza la sentencia lógica and para verificar si la edad del usuario es mayor o igual a 18 y si compró la película. El resultado se asigna a la variable puede_ver_pelicula.

#### Línea 25: 
if puede_ver_pelicula:

Esta línea utiliza la sentencia condicional if para verificar si la variable puede_ver_pelicula es verdadera. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque if.

#### Línea 25: 
print ("Puedes Ver La Película")

Esta línea se ejecuta si la condición puede_ver_pelicula es verdadera. Imprime el mensaje "Puedes Ver La Película" en la pantalla.

#### Línea 26: 
else: print ("No Puedes Ver La Película")

Esta línea se ejecuta si la condición puede_ver_pelicula es falsa. Imprime el mensaje "No Puedes Ver La Película" en la pantalla.

#### Línea 28: 
print ("¡Garcias Por Usar Netflix!")

Esta línea imprime un mensaje de agradecimiento en la pantalla.

