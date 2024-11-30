## PROGRAMA 8 QUE PERMITE CONVERTIR DÍAS A HORAS, MINUTOS Y MESES
En este programa, se permite al usuario convertir un número de días a horas, minutos y meses. El programa solicita al usuario que ingrese el número de días y luego realiza las conversiones necesarias para mostrar los resultados.
### Explicación Del Programa:

#### Línea 5:
dias = int(input("Solicita El Numero De Días: "))

Esta línea utiliza la función input para solicitar al usuario que ingrese el número de días. La función int se utiliza para convertir la entrada del usuario en un número entero.

#### Línea 6:
horas = int ((dias*24))

Esta línea calcula el número de horas equivalentes al número de días ingresado por el usuario. Se multiplica el número de días por 24 para obtener el número de horas.

#### Línea 7:
minutos = int ((horas*60))

Esta línea calcula el número de minutos equivalentes al número de horas calculado en la línea anterior. Se multiplica el número de horas por 60 para obtener el número de minutos.

#### Línea 8:
meses = float ((dias/30))

Esta línea calcula el número de meses equivalentes al número de días ingresado por el usuario. Se divide el número de días por 30 para obtener el número de meses. La función float se utiliza para convertir el resultado en un número decimal.

#### Línea 10:
print ("El Numero De Días Es: " + str(dias))

Esta línea utiliza la función print para mostrar el número de días ingresado por el usuario. La función str se utiliza para convertir el número de días en una cadena de texto que se puede concatenar con el mensaje.

#### Línea 11:
print ("El Numero De Horas Es: " + str(horas))

Esta línea utiliza la función print para mostrar el número de horas calculado. La función str se utiliza para convertir el número de horas en una cadena de texto que se puede concatenar con el mensaje.

#### Línea 12:
print ("El Numero De Minutos Es: " + str( minutos ))

Esta línea utiliza la función print para mostrar el número de minutos calculado. La función str se utiliza para convertir el número de minutos en una cadena de texto que se puede concatenar con el mensaje.

#### Línea 13:
print ("El Numero De Meses Es: " + str(meses))

Esta línea utiliza la función print para mostrar el número de meses calculado. La función str se utiliza para convertir el número de meses en una cadena de texto que se puede concatenar con el mensaje.
