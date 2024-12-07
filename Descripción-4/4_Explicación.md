# 4_PROGRAMA QUE MUESTRA EL USO DE UN CICLO FOR PARA ITERAR SOBRE UNA LISTA Y ACCEDER A SUS ELEMENTOS
Este programa muestra cómo se puede utilizar un ciclo for para iterar sobre una lista y acceder a sus elementos.
## Explicación: 
Línea 1: Esta línea crea una lista llamada "personajes" que contiene 10 elementos: "Goku", "Vegeta", "Trunks", "Piccolo", "Gohan", "Krilin", "Bulma", "Yamcha", "Tenshinhan" y "Freezer". La lista se define utilizando corchetes `[]` y los elementos se separan con comas.
- "personajes" es el nombre de la variable que se utiliza para almacenar la lista.
- "=[Goku, Vegeta, Trunks, Piccolo, Gohan, Krilin, Bulma, Yamcha, Tenshinhan, Freezer]" es la asignación de la lista a la variable "personajes".
- "[Goku, Vegeta, Trunks, Piccolo, Gohan, Krilin, Bulma, Yamcha, Tenshinhan, Freezer]" es la lista en sí, que contiene 10 elementos.

```python
personajes = ["Goku", "Vegeta", "Trunks", "Piccolo", "Gohan", "Krilin", "Bulma", "Yamcha", "Tenshinhan", "Freezer"]
```

Línea 2: Esta línea comienza un `ciclo for` que itera sobre la lista "personajes". La variable `i` toma el valor de cada índice de la lista durante cada iteración. El `ciclo for` utiliza la función `len()` para obtener la longitud de la lista y la `función range()` para generar una secuencia de números que va desde 0 hasta la longitud de la lista.
- "for" es la palabra clave que se utiliza para comenzar un `ciclo for`.
- "i" es la variable que se utiliza para almacenar el valor de cada índice de la lista durante cada iteración.
- "in range(len(personajes))" es la expresión que se utiliza para especificar la secuencia de números que se va a iterar.
  
```python
for i in range(len(personajes)):
```

Línea 3. Esta línea imprime un mensaje que incluye el valor de la variable "i+1" y el valor del elemento en la lista "personajes" que corresponde al índice "i". La variable "i+1" se utiliza para mostrar el número del personaje, comenzando desde 1 en lugar de 0.
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "f" es el prefijo que se utiliza para indicar que la cadena es una cadena `f (formatted string)`.
- `Personaje {i+1}: {personajes[i]}` es la cadena que se utiliza para mostrar el mensaje. La cadena incluye las variables `i+1` y `personajes[i]`, que se reemplazan con sus valores correspondientes durante la impresión.


```python
print(f"Personaje {i+1}: {personajes[i]}")
```

El resultado del programa será la impresión de la lista de personajes, con cada personaje numerado comenzando desde 1. Por ejemplo:

Personaje 1: Goku
Personaje 2: Vegeta
Personaje 3: Trunks
Personaje 4: Piccolo
Personaje 5: Gohan
Personaje 6: Krilin
Personaje 7: Bulma
Personaje 8: Yamcha
Personaje 9: Tenshinhan
Personaje 10: Freezer
