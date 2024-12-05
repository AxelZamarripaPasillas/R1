# 4_PROGRAMA QUE CALCULA LOS IMPUESTOS DE UN VALOR
Programa que calcula el valor de impuestos sobre un valor ingresado por el usuario.

## Explicación Del Programa:
Este programa solicita al usuario que ingrese un valor y luego calcula el valor de impuestos correspondiente. El programa utiliza una tasa de impuesto del 25%.

## PRIMER PROGRAMA

Línea 6:  Esta línea utiliza la función `input()` para solicitar al usuario que ingrese un valor. La función `float()` se utiliza para convertir la entrada del usuario en un número flotante.

```python
valor= (float(input("Ingrese EL Valor: ")))
```

Línea 7: Esta línea calcula el valor de los impuestos multiplicando el valor ingresado por el usuario por `0.25 (25%)`.

```python
valor_con_impuestos = (0.25*valor)
```

Línea 8: Esta línea utiliza la función `print()` para mostrar el valor de los impuestos calculado en la línea anterior.

```python
print("El Valor De Impuestos Es: ", valor_con_impuestos)
```

Línea 9:  Esta línea utiliza la función `print()` para mostrar un mensaje de agradecimiento al usuario.

```python
print ("¡Gracias Por Usar Nuestro Sistema!")
```

## SEGUNDO PROGRAMA

Línea 12: Esta línea utiliza la función `print()` para mostrar el valor de los impuestos calculado en tiempo real. La función `float()` se utiliza para convertir la entrada del usuario en un número flotante. La expresión `* 0.25` calcula el valor de los impuestos multiplicando el valor ingresado por el usuario por `0.25 (25%)`. La expresión `:.2f` formatea el resultado como un número flotante con dos decimales.

```python
print (f"Los impuestos son: $ {float(input('Ingrese el valor: '))* 0.25:.2f}")
```

