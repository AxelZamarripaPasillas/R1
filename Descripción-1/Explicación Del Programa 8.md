# 8_PROGRAMA QUE PERMTE HACER OPERACIONES BASICAS (+, -, * y /)
Programa que realiza operaciones aritméticas básicas entre dos números ingresados por el usuario.
## Explicación Del Programa:

Línea 4: Esta línea utiliza la función `Input()` para solicitar al usuario que ingrese el primer número. La función `int()` se utiliza para convertir la entrada del usuario en un número entero.

```python
num1 = int(input("Ingresa El Primer Numero:"))
```

Línea 5: Esta línea utiliza la función `Input()` para solicitar al usuario que ingrese el segundo número. La función `int()` se utiliza para convertir la entrada del usuario en un número entero.

```python
num2 = int(input("Ingresa El Segundo Numero:"))
```

Línea 6: Esta línea calcula la suma de los dos números ingresados por el usuario.

```python
suma = num1 + num2
```

Línea 7: Esta línea calcula la resta de los dos números ingresados por el usuario.

```python
resta = num1 - num2
```

Línea 8: Esta línea calcula la multiplicación de los dos números ingresados por el usuario.

```python
multiplicacion = num1 * num2
```

Línea 9: Esta línea calcula la división de los dos números ingresados por el usuario. Sin embargo, es importante tener en cuenta que si el usuario ingresa un valor de 0 para el segundo número, el programa producirá un error de división por cero.

```python
division = num1 / num2
```

Línea 11: Esta línea utiliza la función `Print()` para mostrar el resultado de la suma. La función `str` se utiliza para convertir el resultado en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El valor De La Suma Es:"+ str(suma))
```

Línea 12: Esta línea utiliza la función `Print()` para mostrar el resultado de la resta. La función `str()` se utiliza para convertir el resultado en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El valor De La Resta Es:"+ str(resta))
```

Línea 13: Esta línea utiliza la función `Print()` para mostrar el resultado de la multiplicación. La función `str()` se utiliza para convertir el resultado en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El valor De La Multiplicación Es:"+ str(multiplicacion))
```

Línea 14: Esta línea utiliza la función `Print()` para mostrar el resultado de la división. La función `str()` se utiliza para convertir el resultado en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El valor De La División Es:"+ str(division))
```

