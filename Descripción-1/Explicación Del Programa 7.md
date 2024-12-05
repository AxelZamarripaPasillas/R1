# 7_PROGRAMA QUE PERMITE CALCULAR EL PERIMETRO Y EL ÁREA DE UN CÍRCULO
Este programa de cálculo geométrico permite determinar el perímetro y el área de un círculo cuando se conoce su radio. Solicita al usuario que ingrese el radio del círculo, realiza los cálculos correspondientes y muestra en pantalla el perímetro y el área del círculo.
## Explicación Del Programa: 

Línea 5: Esta línea utiliza la función `Print()` para mostrar un mensaje que describe el propósito del programa.

```python
print ("Programa Que Permite Calcular El Perimetro y El Área De Un Círculo")
```

Línea 7: Esta línea utiliza la función `Input()` para solicitar al usuario que ingrese el radio del círculo. La función `Float()` se utiliza para convertir la entrada del usuario en un número flotante.

```python
radio = float(input("Ingrese El Radio Del Circulo: "))
```

Línea 9: Esta línea calcula el perímetro del círculo utilizando la fórmula `2πr`, donde `r` es el radio del círculo.

```python
PerimetroCirculo = (2*radio*3.14)
```

Línea 10: Esta línea calcula el área del círculo utilizando la fórmula `πr^2`, donde `r` es el radio del círculo. 

```python
AreaCirculo = (3.14*radio)**2
```

Línea 12: Esta línea utiliza la función `Print()` para mostrar el resultado del cálculo del perímetro del círculo.

```python
print ("El Perimetro Del Circulo es:", PerimetroCirculo)
```

Línea 13: Esta línea utiliza la función `Print()` para mostrar el resultado del cálculo del área del círculo.

```python
print ("El Área Del Circulo es:", AreaCirculo)
```

