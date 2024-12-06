# 2_PROGRAMA QUE DEMUESTRA LA CONVERSIÓN DE TIPOS DE DATOS
Este programa solicita al usuario que ingrese su edad y luego muestra el tipo de dato de la variable en diferentes momentos, demostrando la conversión de tipos de datos.

## Explicación:

Línea 1: Esta línea utiliza la función `input()` para solicitar al usuario que ingrese su edad. La entrada del usuario se almacena en la variable `variable`.

```python
variable = input("Ingresa Tu Edad: ")
```

Línea 2: Esta línea imprime el tipo de dato de la variable ‘variable’ utilizando la función `type()`.

```python
print (type(variable))
```

Línea 3: Esta línea convierte la variable a tipo entero utilizando la función `int()`.

```python
variable = int(variable)
```

Línea 4: Esta línea imprime el tipo de dato de la variable ‘variable’ después de la conversión a tipo entero.

```python
print (type(variable))
```

Línea 5: Esta línea convierte la variable `variable` a tipo flotante utilizando la función `float()`.

```python
variable = float (variable)
```

Línea 6: Esta línea imprime el tipo de dato de la variable `variable` después de la conversión a tipo flotante.

```python
print (type(variable))
```
