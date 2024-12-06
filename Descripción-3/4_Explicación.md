# 4_PROGRAMA QUE CALCULE LOS IMPUESTOS QUE DEBE PAGAR UN EMPLEADO
Este programa solicita al usuario que ingrese sus ingresos y luego calcula el salario final después de impuestos, según una escala de impuestos determinada.

## Explicación: 
Línea 1: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese sus ingresos. La entrada del usuario se almacena en la variable `ingresos` y se convierte 
a tipo flotante utilizando la función `float()`.

```python
ingresos = float(input("¿Cuáles Son Tus Ingresos? "))
```

Línea 2-5: Esta sección utiliza una estructura de control condicional `if-elif-else` para calcular el impuesto según la escala de impuestos determinada.

```python
if ingresos <= 1000.0:
    impuestos = ingresos * 0.05
elif ingresos > 1000.0 and ingresos <= 2500:
    impuestos = ingresos * 0.08
elif ingresos > 2500.0 and ingresos <= 6000:
    impuestos = ingresos * 0.12
else:
    impuestos = ingresos * 0.15
```

Línea 6
Esta línea calcula el salario final después de impuestos restando el impuesto de los ingresos.

```python
salario_total = (ingresos - impuestos)
```

Línea 7
Esta línea imprime el impuesto y el salario final después de impuestos utilizando la función `print()`.

```python
print ("Tus Impuestos Son:" + str(impuestos) + " y Tu Salario Final Es " + str(salario_total))
```
