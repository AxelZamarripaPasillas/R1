# 5_THE SUM PATTERN
Este patrón se utiliza para calcular la suma de una serie de números.
## Explicación: 
Línea 1: Esta línea crea una lista llamada "numeros" que contiene cuatro elementos: 100, 200, 300 y 400.
- "numeros" es el nombre de la variable que se utiliza para almacenar la lista.
- "=[100, 200, 300, 400]" es la asignación de la lista a la variable "numeros".
- "[100, 200, 300, 400]" es la lista en sí, que contiene cuatro elementos.

```python
numeros = [100, 200, 300, 400]
```

Línea 2: Esta línea inicializa una variable llamada "sumatoria" con un valor de 0. Esta variable se utilizará para almacenar la suma de los números en la lista.
- "sumatoria" es el nombre de la variable que se utiliza para almacenar la suma.
- "= 0" es la asignación del valor inicial a la variable "sumatoria".

```python
sumatoria = 0
```

Línea 3: Esta línea comienza un `ciclo for` que itera sobre la lista "numeros". La variable "numero" toma el valor de cada número en la lista durante cada iteración.
- "for" es la palabra clave que se utiliza para comenzar un `ciclo for`.
- "numero" es la variable que se utiliza para almacenar el valor de cada número en la lista durante cada iteración.
- "in numeros" es la expresión que se utiliza para especificar la lista que se va a iterar.
  
```python
for numero in numeros:
```

Línea 4: Esta línea suma el valor de la variable "numero" a la variable "sumatoria" durante cada iteración del `ciclo for`.
- "sumatoria" es la variable que se utiliza para almacenar la suma.
- "= sumatoria + numero" es la expresión que se utiliza para sumar el valor de la variable "numero" a la variable "sumatoria".

```python
sumatoria = sumatoria + numero
```

Línea 5: Esta línea imprime el valor final de la variable "sumatoria", que es la suma de todos los números en la lista.
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "La Sumatoria Es" es el mensaje que se imprime antes del valor de la variable "sumatoria".
- "sumatoria" es la variable que se utiliza para almacenar la suma.
  
```python
print ("La Sumatoria Es", sumatoria)
```

# The Accumulation Pattern
Este patrón se utiliza para acumular una serie de valores en una variable.
## Explicación: 
Línea 1: Esta línea crea una lista llamada "palabras" que contiene cinco elementos: "Hoy", " ", "Hace", " ", "Frío".
- "palabras" es el nombre de la variable que se utiliza para almacenar la lista.
- "=[Hoy,  , Hace,  , Frío]" es la asignación de la lista a la variable "palabras".
- "[Hoy,  , Hace,  , Frío]" es la lista en sí, que contiene cinco elementos.

```python
palabras = ["Hoy", " ", "Hace", " ", "Frío"]
```

Línea 2: Esta línea inicializa una variable llamada "mensaje" con un valor vacío. Esta variable se utilizará para almacenar el mensaje acumulado.
- "mensaje" es el nombre de la variable que se utiliza para almacenar el mensaje.
- "= """ es la asignación del valor inicial a la variable "mensaje".

```python
mensaje = ""
```

Línea 3: Esta línea comienza un `ciclo for` que itera sobre la lista "palabras". La variable "palabra" toma el valor de cada palabra en la lista durante cada iteración.
- "for" es la palabra clave que se utiliza para comenzar un `ciclo for`.
- "palabra" es la variable que se utiliza para almacenar el valor de cada palabra en la lista durante cada iteración.
- "in palabras" es la expresión que se utiliza para especificar la lista que se va a iterar.
  
```python
for palabra in palabras:
```

Línea 4: Esta línea acumula el valor de la variable "palabra" en la variable "mensaje" durante cada iteración del `ciclo for`.
- "mensaje" es la variable que se utiliza para almacenar el mensaje.
- "= mensaje + palabra" es la
  
```python
mensaje = mensaje + palabra
```

