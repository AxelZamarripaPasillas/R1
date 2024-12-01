## PROGRAMA QUE CALCULA LOS IMPUESTOS DE UN VALOR
En este programa, se calculan los impuestos de un valor ingresado por el usuario.

### Explicación Del Programa:

### PRIMER PROGRAMA

#### Línea 5: 
valor= (float(input("Ingrese EL Valor: ")))

Esta línea utiliza la función input para solicitar al usuario que ingrese un valor. La función float se utiliza para convertir la entrada del usuario en un número flotante.

#### Línea 6: 
valor_con_impuestos = (0.25*valor)

Esta línea calcula el valor de los impuestos multiplicando el valor ingresado por el usuario por 0.25 (25%).

#### Línea 7: 
print("El Valor De Impuestos Es: ", valor_con_impuestos)

Esta línea utiliza la función print para mostrar el valor de los impuestos calculado en la línea anterior.

#### Línea 8: 
print ("¡Gracias Por Usar Nuestro Sistema!")

Esta línea utiliza la función print para mostrar un mensaje de agradecimiento al usuario.

### SEGUNDO PROGRAMA

#### Línea 10: 
print (f"Los impuestos son: $ {float(input('Ingrese el valor: '))* 0.25:.2f}")

Esta línea utiliza la función print para mostrar el valor de los impuestos calculado en tiempo real. La función float se utiliza para convertir la entrada del usuario en un número flotante. La expresión * 0.25 calcula el valor de los impuestos multiplicando el valor ingresado por el usuario por 0.25 (25%). La expresión :.2f formatea el resultado como un número flotante con dos decimales.
