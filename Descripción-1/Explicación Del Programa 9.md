# PROGRAMA 9
Programa que convierte un número de días en horas, minutos y meses. 
## Explicación Del Programa:
Este programa solicita al usuario que ingrese un número de días y luego realiza las conversiones necesarias para expresar ese número en horas, minutos y meses.

Línea 5: Esta línea utiliza la función `Input` para solicitar al usuario que ingrese el número de días. La función `int` se utiliza para convertir la entrada del usuario en un número entero.

```python
dias = int(input("Solicita El Numero De Días: "))
```

Línea 6: Esta línea calcula el número de horas equivalentes al número de días ingresado por el usuario. Se multiplica el número de días por 24 para obtener el número de horas.

```python
horas = int ((dias*24))
```

Línea 7: Esta línea calcula el número de minutos equivalentes al número de horas calculado en la línea anterior. Se multiplica el número de horas por 60 para obtener el número de minutos.

```python
minutos = int ((horas*60))
```

Línea 8:  Esta línea calcula el número de meses equivalentes al número de días ingresado por el usuario. Se divide el número de días por 30 para obtener el número de meses. La función `float` se utiliza para convertir el resultado en un número decimal.

```python
meses = float ((dias/30))
```

Línea 10: Esta línea utiliza la función `print` para mostrar el número de días ingresado por el usuario. La función `str` se utiliza para convertir el número de días en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El Numero De Días Es: " + str(dias))
```

Línea 11: Esta línea utiliza la función `print` para mostrar el número de horas calculado. La función `str` se utiliza para convertir el número de horas en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El Numero De Horas Es: " + str(horas))
```

Línea 12: Esta línea utiliza la función `print` para mostrar el número de minutos calculado. La función `str` se utiliza para convertir el número de minutos en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El Numero De Minutos Es: " + str( minutos ))
```

Línea 13:  Esta línea utiliza la función `print` para mostrar el número de meses calculado. La función `str` se utiliza para convertir el número de meses en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El Numero De Meses Es: " + str(meses))
```
