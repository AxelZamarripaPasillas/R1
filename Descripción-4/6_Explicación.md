Programa que crea una nueva lista con números menores a 50

Este programa muestra cómo se puede utilizar un ciclo for y una condición if para crear una nueva lista con números menores a 50.

Línea 1
Esta línea crea una lista llamada "numeros" que contiene 10 elementos: 10, 50, 25, 13, 10, 28, 100, 500, 29 y 27.


numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 27]


- "numeros" es el nombre de la variable que se utiliza para almacenar la lista.
- "=[10, 50, 25, 13, 10, 28, 100, 500, 29, 27]" es la asignación de la lista a la variable "numeros".
- "[10, 50, 25, 13, 10, 28, 100, 500, 29, 27]" es la lista en sí, que contiene 10 elementos.

Línea 2
Esta línea crea una lista vacía llamada "menores_50". Esta lista se utilizará para almacenar los números menores a 50.


menores_50 = []


- "menores_50" es el nombre de la variable que se utiliza para almacenar la lista vacía.
- "= []" es la asignación de la lista vacía a la variable "menores_50".

Línea 3
Esta línea comienza un ciclo for que itera sobre la lista "numeros". La variable "numero" toma el valor de cada número en la lista durante cada iteración.


for numero in numeros:


- "for" es la palabra clave que se utiliza para comenzar un ciclo for.
- "numero" es la variable que se utiliza para almacenar el valor de cada número en la lista durante cada iteración.
- "in numeros" es la expresión que se utiliza para especificar la lista que se va a iterar.

Línea 4
Esta línea evalúa si el número actual es menor a 50. Si la condición es verdadera, se ejecuta la línea siguiente.


if numero < 50:


- "if" es la palabra clave que se utiliza para evaluar una condición.
- "numero < 50" es la condición que se evalúa.

Línea 5
Esta línea agrega el número actual a la lista "menores_50" si la condición en la línea anterior es verdadera.


menores_50.append (numero)


- "menores_50" es la lista a la que se agrega el número.
- "append" es el método que se utiliza para agregar un elemento a la lista.
- "(numero)" es el argumento que se pasa al método "append".

Línea 6
Esta línea imprime la lista original "numeros".


print ("La Lista Original Es:", numeros)


- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "La Lista Original Es:" es el mensaje que se imprime antes de la lista.
- "numeros" es la lista que se imprime.

Línea 7
Esta línea imprime la lista "menores_50" que contiene los números menores a 50.


print ("La Nueva Lista Es:", menores_50)


- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "La Nueva Lista Es:" es el mensaje que se imprime antes de la lista.
- "menores_50" es la lista que se imprime.
