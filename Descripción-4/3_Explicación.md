# 3_PROGRAMA QUE MUESTRA EL USO DE LA FUNCIÓN RANGE PARA GENERAR SECUENCIAS DE NÚMEROS
Este programa muestra cómo se puede utilizar la función range para generar secuencias de números y luego imprimirlos utilizando un `ciclo for`.
## Explicación:
Línea 1: Esta línea imprime un mensaje que indica que se van a imprimir los valores del 0 al 9.

```python
print ("Imprime Los Valores Del 0 al 9")
```

Línea 2: Esta línea utiliza la función range para generar una secuencia de números que comienza en 0 y termina en 9. La función range devuelve un objeto iterable que se puede utilizar en un `ciclo for`.
-"x" es la variable que se utiliza para almacenar el objeto iterable devuelto por la función `range`.
- "range(10)" es la llamada a la `función range` que genera la secuencia de números.

```python
x = range (10)
```


Línea 3: Esta línea comienza un `ciclo for` que itera sobre la secuencia de números generada por la función range. La variable "num" toma el valor de cada número en la secuencia durante cada iteración.
- "for" es la palabra clave que se utiliza para comenzar un `ciclo for`.
- "num" es la variable que se utiliza para almacenar el valor de cada número en la secuencia durante cada iteración.
- "in x" es la expresión que se utiliza para especificar la secuencia de números que se va a iterar.

```python
for num in x:
```

Línea 4: Esta línea imprime el valor de la variable "num" durante cada iteración del `ciclo for`.
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "num" es la variable que se utiliza para almacenar el valor de cada número en la secuencia durante cada iteración.

```python
print (num)
```

Línea 5: Esta línea imprime un mensaje que indica que se van a imprimir los valores del 5 al 15.

```python
print ("\nImprime Los Valores Del 5 Al 15")
```

Línea 6: Esta línea utiliza la `función range` para generar una secuencia de números que comienza en 5 y termina en 15. La `función range` devuelve un objeto iterable que se puede utilizar en un `ciclo for`.
- "x1" es la variable que se utiliza para almacenar el objeto iterable devuelto por la `función range`.
- "range(5, 16)" es la llamada a la función range que genera la secuencia de números.

```python
x1 = range (5, 16)
```

Línea 7: Esta línea comienza un `ciclo for` que itera sobre la secuencia de números generada por la `función range`. La variable "num" toma el valor de cada número en la secuencia durante cada iteración.

```python
for num in x1:
```

Línea 8: Esta línea imprime el valor de la variable "num" durante cada iteración del `ciclo for`.

```python
print (num)
```

Línea 9: Esta línea imprime un mensaje que indica que se van a imprimir los valores del 10 al 20.

```python
print ("\nImprime Los Valores Del 10 Al 20")
```

Línea 10
Esta línea utiliza la `función range` para generar una secuencia de números que comienza en 10 y termina en 20, con un paso de 2. La `función range` devuelve un objeto iterable que se puede utilizar en un `ciclo for`.
- "x2" es la variable que se utiliza para almacenar el objeto iterable devuelto por la `función range`.
- "range(10, 21, 2)" es la llamada a la función range que genera la secuencia de números.
  
```python
x2 = range (10, 21, 2)
```

Línea 11: Esta línea comienza un `ciclo for` que itera sobre la secuencia de números generada por la `función range`. La variable "num" toma el valor de cada número en la secuencia durante cada iteración.

```python
for num in x2:
```

Línea 12: Esta línea imprime el valor de la variable "num" durante cada iteración del `ciclo for`.

```python
print (num)
```

Línea 13: Esta línea imprime un mensaje que indica que se van a imprimir los valores del 11 al 21.

```python
print ("\nImprime Los Valores Del 11 Al 21")
```

Línea 14: Esta línea utiliza la `función range` para generar una secuencia de números que comienza en 11 y termina en 21, con un paso de 2. La función range devuelve un objeto iterable que se puede utilizar en un `ciclo for`.
- "x3" es la variable que se utiliza para almacenar el objeto iterable devuelto por la `función range`.
- "range(11, 22, 2)" es la llamada a la función range que genera la secuencia de números.

```python
x3 = range (11, 22, 2)
```


Línea 15: Esta línea comienza un `ciclo for` que itera sobre la secuencia de números generada por la `función range`. La variable "num" toma el valor de cada número en la secuencia durante cada iteración.
- "for" es la palabra clave que se utiliza para comenzar un `ciclo for`.
- "num" es la variable que se utiliza para almacenar el valor de cada número en la secuencia durante cada iteración.
- "in x3" es la expresión que se utiliza para especificar la secuencia de números que se va a iterar.

```python
for num in x3:
```

Línea 16: Esta línea imprime el valor de la variable "num" durante cada iteración del `ciclo for`.
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "num" es la variable que se utiliza para almacenar el valor de cada número en la secuencia durante cada iteración.

```python
print (num)
```

El resultado del programa será la impresión de las secuencias de números generadas por la función range, con los mensajes correspondientes.
