## PROGRAMA DE CONDICIONAL IF
Este programa solicita al usuario que ingrese la cantidad de artículos comprados y calcula el total a pagar según la cantidad. Si la cantidad es mayor que 3, se aplica un descuento y el total se calcula multiplicando la cantidad por 30. De lo contrario, el total se calcula multiplicando la cantidad por 45. En este programa, se muestra cómo utilizar la sentencia condicional if para tomar decisiones basadas en una condición. En este caso, se calcula el total a pagar por una cantidad de artículos comprados. 
### Explicación Del Programa:
#### Línea 4: 
cantidad = int (input("¿Cuántos Artículos Compró?"))

Esta línea utiliza la función input para solicitar al usuario que ingrese la cantidad de artículos comprados. La función int se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable cantidad.

#### Línea 6: 
if cantidad >3:

Esta línea utiliza la sentencia condicional if para verificar si la cantidad de artículos comprados es mayor que 3. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque if.

#### Línea 7: 
total= cantidad * 30

Esta línea se ejecuta si la condición cantidad >3 es verdadera. Calcula el total a pagar multiplicando la cantidad de artículos comprados por 30.

#### Línea 8: 
else:

Esta línea utiliza la sentencia else para especificar el código que se ejecutará si la condición cantidad >3 es falsa.

#### Línea 9: 
total = cantidad * 45

Esta línea se ejecuta si la condición cantidad >3 es falsa. Calcula el total a pagar multiplicando la cantidad de artículos comprados por 45.

#### Línea 10: 
print ("El Total a Pagar Es $" + str(total))

Esta línea imprime el total a pagar calculado en las líneas anteriores. La función str se utiliza para convertir el valor de total en una cadena de texto.

#### Línea 11: 
print("Saludo...")

Esta línea imprime un mensaje de saludo en la pantalla.


