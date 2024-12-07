Inicialización de variable

Este programa muestra cómo se puede utilizar un ciclo while para pedir al usuario que ingrese palabras hasta que ingrese la palabra "salir".

Línea 1
Esta línea inicializa una variable llamada "palabra" con un valor vacío.


palabra = ""


- "palabra" es el nombre de la variable que se utiliza para almacenar la palabra ingresada por el usuario.
- "= """ es la asignación del valor vacío a la variable "palabra".

Línea 2
Esta línea comienza un ciclo while que se ejecutará mientras la variable "palabra" no sea igual a "salir".


while palabra != "salir":


- "while" es la palabra clave que se utiliza para comenzar un ciclo while.
- "palabra != "salir"" es la condición que se evalúa para determinar si se ejecuta el código dentro del ciclo while.

Línea 3
Esta línea pide al usuario que ingrese una palabra o la palabra "salir" para terminar.


palabra = input ("Ingresa Una Palabra o 'salir' Para Terminar: ")


- "input" es la función que se utiliza para pedir al usuario que ingrese un valor.
- "Ingresa Una Palabra o 'salir' Para Terminar: " es el mensaje que se muestra al usuario para que ingrese una palabra.
- "palabra" es la variable que se utiliza para almacenar la palabra ingresada por el usuario.

Línea 4
Esta línea convierte la palabra ingresada por el usuario a minúsculas utilizando el método "lower()".


palabra = palabra.lower ()


- "palabra.lower ()" es el método que se utiliza para convertir la palabra ingresada por el usuario a minúsculas.
- "palabra" es la variable que se utiliza para almacenar la palabra en minúsculas.

Línea 5
Esta línea imprime la palabra ingresada por el usuario en minúsculas.


print ("Usted Ingreso:", palabra)


- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "Usted Ingreso: " es el mensaje que se muestra antes de imprimir la palabra ingresada por el usuario.
- "palabra" es la variable que se imprime.

Línea 6
Esta línea imprime un mensaje que indica el final del programa.


print ("Fin Del Programa")


- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "Fin Del Programa" es el mensaje que se imprime.
