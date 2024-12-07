# 9_UTILIZANDO LA FUNCIÓN BRAKE Y LA FUNCIÓN CONTINUE
La función break se utiliza para salir de un ciclo (while o for) de manera inmediata, sin ejecutar el resto del código dentro del ciclo. La función continue, por otro lado, se utiliza para saltar al siguiente ciclo, omitiendo el resto del código dentro del ciclo actual. En otras palabras, continue hace que el ciclo continúe con la siguiente iteración, sin ejecutar el código restante del ciclo actual.
## Explicación:
### Ejemplo 1: Uso de la instrucción break
Línea 1: Esta línea inicializa una variable llamada "i" con un valor de 1.
- "i" es el nombre de la variable que se utiliza para almacenar el valor del contador.
- "= 1" es la asignación del valor inicial a la variable "i".

```python
i = 1
```

Línea 2: Esta línea comienza la estructura `while`. La condición de la estructura while es que `i` sea menor o igual a 10.
- "while" es la palabra clave que se utiliza para comenzar una estructura `while`.
- "i <= 10" es la condición que se evalúa para determinar si se ejecuta el código dentro de la estructura `while`.

```python
while i <= 10:
```

Línea 3: Esta línea evalúa si el valor actual de "i" es igual a 5. Si es cierto, se ejecuta la instrucción `break`.
- "if" es la palabra clave que se utiliza para evaluar una condición.
- "i == 5" es la condición que se evalúa.
- "break" es la instrucción que se ejecuta si la condición es cierta, lo que hace que se salga de la estructura `while`.

```python
if i == 5:
    break
```

Línea 4: Esta línea imprime el valor actual de la variable "i".
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "(i)" es el argumento que se pasa a la función "print", que es el valor actual de la variable "i".

```python
print(i)
```

Línea 5: Esta línea incrementa el valor de la variable "i" en 1.
- "i" es la variable que se incrementa.
- "+= 1" es la operación que se realiza para incrementar el valor de la variable "i" en 1.

```python
i += 1
```

Línea 6: Esta línea imprime un mensaje que indica el final del programa.
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "Fin Del Programa" es el mensaje que se imprime.

```python
print("Fin Del Programa")
```

### Ejemplo 2: Uso de la instrucción continue
Línea 1: Esta línea inicializa una variable llamada "i" con un valor de 1.
- "i" es el nombre de la variable que se utiliza para almacenar el valor del contador.
- "= 1" es la asignación del valor inicial a la variable "i".
  
```python
i = 1
```

Línea 2: Esta línea comienza la estructura `while`. La condición de la estructura `while` es que "i" sea menor o igual a 10.
- "while" es la palabra clave que se utiliza para comenzar una estructura `while`.
- "i <= 10" es la condición que se evalúa para determinar si se ejecuta el código dentro de la estructura `while`.
  
```python
while i <= 10:
```

Línea 3: Esta línea evalúa si el valor actual de "i" es igual a 5. Si es cierto, se ejecuta la instrucción continue.
- "if" es la palabra clave que se utiliza para evaluar una condición.
- "i == 5" es la condición que se evalúa.
- "continue" es la instrucción que se ejecuta si la condición es cierta, lo que hace que se salte el resto del código dentro de la estructura `while` y se pase a la siguiente iteración.

```python
if i == 5:
    continue
```

Línea 4: Esta línea imprime el valor actual de la variable "i".
- "print" es la función que se utiliza para imprimir el resultado en la consola.
- "(i)" es el argumento que se pasa a la función "print", que es el valor actual de la variable "i".
  
```python
print(i)
```

Línea 5: Esta línea incrementa el valor de la variable "i" en 1.
- "i" es la variable que se incrementa.
- "+= 1" es la operación que se realiza para incrementar el valor de la variable "i" en 1.

```python
i += 1
```

Línea 6: Esta línea imprime un mensaje

```python
print ("Gracias Por Usar Nuestro Programa")
```
