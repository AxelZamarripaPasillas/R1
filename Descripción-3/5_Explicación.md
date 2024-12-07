# 5_PROGRAMA QUE CALCULA EL NIVEL DE DESEMPEÑO DE UN ESTUDIANTE
Este programa solicita al usuario que ingrese su calificación final y luego calcula el nivel de desempeño del estudiante según una escala determinada.
## Explicación Del Programa: 
Línea 1: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese su calificación final. La entrada del usuario se almacena en la variable `cal`
y se convierte a tipo flotante utilizando la función `float()`.

```python
cal = float(input("¿Cuál Es Tu Calificación Final? "))
```

Línea 2-9: Esta sección utiliza una estructura de control condicional `if-elif-else` para calcular el nivel de desempeño del estudiante según la calificación ingresada.

```python
if cal <= 60.0:
    print ("Insuficiente")
elif cal >= 70.0 or cal < 80.0:
    print ("Suficiente")
elif cal >=80.0 or cal <90.0:
    print ("Muy Bien")
elif cal >=90.0 or cal <96.0:
    print ("Notable")
else:
    print ("Excelente")
```

Línea 10: Esta línea imprime un mensaje de agradecimiento al usuario por utilizar el programa utilizando la función `print()`.

```python
print ("¡Gracias Por Usar Nuestro Programa!")
```
