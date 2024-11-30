## PROGRAMA 6 QUE PERMITE CALCULAR EL PERIMETRO Y EL ÁREA DE UN CÍRCULO
En este programa, se calculan el perímetro y el área de un círculo utilizando las fórmulas matemáticas correspondientes. El programa solicita al usuario que ingrese el radio del círculo y luego calcula y muestra el perímetro y el área del círculo.
### Explicación Del Programa: 

#### Línea 5:

print ("Programa Que Permite Calcular El Perimetro y El Área De Un Círculo")

Esta línea utiliza la función print para mostrar un mensaje que describe el propósito del programa.

Línea 5:

radio = float(input("Ingrese El Radio Del Circulo: "))

Esta línea utiliza la función input para solicitar al usuario que ingrese el radio del círculo. La función float se utiliza para convertir la entrada del usuario en un número flotante.

Línea 6:

PerimetroCirculo = ( radio*2 * 3.14)**2

Esta línea calcula el perímetro del círculo utilizando la fórmula 2πr, donde r es el radio del círculo. Sin embargo, hay un error en la fórmula, ya que se eleva al cuadrado el resultado de la multiplicación.

Línea 7:

AreaCirculo = (3.14*radio)**2

Esta línea calcula el área del círculo utilizando la fórmula πr^2, donde r es el radio del círculo. Sin embargo, hay un error en la fórmula, ya que se eleva al cuadrado el resultado de la multiplicación.

Línea 8:

print ("El Perimetro Del Circulo es:", PerimetroCirculo)

Esta línea utiliza la función print para mostrar el resultado del cálculo del perímetro del círculo.

Línea 9:

print ("El Área Del Circulo es:", AreaCirculo)

Esta línea utiliza la función print para mostrar el resultado del cálculo del área del círculo.

