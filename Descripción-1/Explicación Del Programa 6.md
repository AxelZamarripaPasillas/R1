# 6_PROGRAMA QUE PERMITE CALCULAR EL ÁREA DE UN TRIÁNGULO 
Este programa permite calcular el perímetro y el área de un círculo dado su radio. El usuario ingresa el valor del radio y el programa muestra los resultados.

## Explicación Del Programa
Línea 5: En esta línea se va a imprimir el mensaje "Solicita La Base y La Altura De Un Triángulo"

```python
print ("Solicita La Base y La Altura De Un Triángulo")
```

Línea 7: Esta línea utiliza la función `Input()` para solicitar al usuario que ingrese la base del triángulo. La función `Float()` se utiliza para convertir la entrada del usuario en un número flotante.

```python
base = float(input("Ingrese La Base Del Triángulo: "))
```

Línea 8: Esta línea utiliza la función `Input()` para solicitar al usuario que ingrese la altura del triángulo. La función `Float()` se utiliza para convertir la entrada del usuario en un número flotante.

```python
altura = float (input("Ingrese La Altura Del Triángulo: "))
```

Línea 9: Esta línea calcula el área del triángulo utilizando la fórmula `base * altura / 2`.

```python
area = (base*altura)/2
```

Línea 11: Esta línea utiliza la función `Print()` para mostrar el resultado del cálculo del área del triángulo. La función `str()` se utiliza para convertir el resultado en una cadena de texto que se puede concatenar con el mensaje.

```python
print ("El Área Del Triángulo Es:" + str(area))
```
