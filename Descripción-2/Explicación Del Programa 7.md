# 7_PROGRAMA DE CONDICIONAL IF
Programa que solicita la edad del usuario y determina si puede entrar a un bar según su edad.
### Explicación Del Programa:
Este programa utiliza una estructura de control condicional (if-else) para determinar si el usuario puede entrar a un bar según su edad.

Línea 5: Esta línea utiliza la función input() para solicitar al usuario que ingrese su edad. La función int() se utiliza para convertir la entrada del usuario en un número entero. El resultado se asigna a la variable "edad".

```python
edad = int (input("INGRESA TU EDAD: "))
```

Línea 7:  Esta línea utiliza la sentencia condicional `if` para verificar si la edad del usuario es mayor o igual a 18. Si la condición es verdadera, se ejecuta el código que se encuentra dentro del bloque `if`.

```python
if edad >=18:
```

Línea 8: Esta línea se ejecuta si la condición edad `>=18` es verdadera. Imprime el mensaje "Puede Entrar Al Bar" en la pantalla.

```python
print("Puede Entrar Al Bar")
```

Línea 9: Esta línea utiliza la sentencia `else` para especificar el código que se ejecutará si la condición edad `>=18` es falsa.

```python
else:
```

Línea 10: Esta línea se ejecuta si la condición edad `>=18` es falsa. Imprime el mensaje "No Puede Entrar Al Bar" en la pantalla.

```python
print("No Puede Entrar Al Bar")
```



