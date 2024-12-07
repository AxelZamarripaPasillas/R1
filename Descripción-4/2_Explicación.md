1_PROGRAMA QUE MUESTRA EL USO DEL CICLO FOR PARA ITERAR SOBRE UNA LISTA

Este programa muestra cómo se puede utilizar el ciclo for para iterar sobre una lista y realizar operaciones con cada elemento.

Línea 1
Esta línea crea una lista llamada "frutas" que contiene tres elementos: "Manza", "Piña" y "Platano". La lista se define utilizando corchetes [] y los elementos se separan con comas.


frutas = ["Manza", "Piña", "Platano"]


- "frutas" es el nombre de la variable que se utiliza para almacenar la lista.
- "=[Manza, Piña, Platano]" es la asignación de la lista a la variable "frutas".
- "[Manza, Piña, Platano]" es la lista en sí, que contiene tres elementos.

Línea 2
Esta línea comienza un ciclo for que itera sobre la lista "frutas". La variable "fruta" toma el valor de cada elemento en la lista durante cada iteración.


for fruta in frutas:


- "for" es la palabra clave que se utiliza para comenzar un ciclo for.
- "fruta" es la variable que se utiliza para almacenar el valor de cada elemento en la lista durante cada iteración.
- "in frutas" es la expresión que se utiliza para especificar la lista que se va a iterar.

Línea 3
Esta línea imprime un mensaje que incluye el valor de la variable "fruta" durante cada iteración del ciclo for.


print ("La Fruta Es:", fruta)


- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "La Fruta Es:" es el mensaje que se imprime antes del valor de la variable "fruta".
- "fruta" es la variable que se utiliza para almacenar el valor de cada elemento en la lista durante cada iteración.

El ciclo for se ejecutará tres veces, una para cada elemento en la lista "frutas". Durante cada iteración, la variable "fruta" tomará el valor del elemento correspondiente en la lista, y se imprimirá el mensaje con el valor de la variable "fruta".

El resultado del programa será:


La Fruta Es: Manza
La Fruta Es: Piña
La Fruta Es: Platano
