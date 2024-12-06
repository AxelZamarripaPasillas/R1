# 3_PROGRAMA QUE COMPARA DOS NÚMEROS
Este programa solicita al usuario que ingrese dos números y luego compara los números para determinar si el primer número es mayor, igual o menor que el segundo número.

Línea 1-2: Esta sección utiliza la función `input()` para solicitar al usuario que ingrese dos números. La entrada del usuario se almacena en las variables `n1` y `n2` y 
se convierte a tipo entero utilizando la función `int()`.

```python
n1 = (int(input("Ingresa El Primer Número: ")))
n2 = (int(input("Ingresa El Segundo Número: ")))
```

Línea 3-8: Esta sección utiliza una estructura de control condicional `if-elif-else` para comparar los números y determinar si el primer número es mayor, igual o menor que 
el segundo número.

```python
if (n1 > n2):
    print(str(n1) + " Es Mayor Que " + str(n2))
elif n1 == n2:
    print(str(n1) + " Es Igual Que " + str(n2))
else:
    print(str(n1) + " Es Menor Que " + str(n2))
```

Línea 9: Esta línea imprime un mensaje de agradecimiento al usuario por utilizar el programa utilizando la función `print()`.

```python
print ("¡Gracias Por Usar Nuestro Programa!")
```
