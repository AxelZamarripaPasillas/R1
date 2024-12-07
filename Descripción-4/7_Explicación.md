Programa que clasifica edades en menores de 18, adultos y mayores de 65

Este programa muestra cómo se puede utilizar un ciclo for y condiciones if-elif-else para clasificar edades en diferentes categorías.

Línea 1
Esta línea crea una lista llamada "edades" que contiene 9 elementos: 45, 56, 32, 14, 78, 34, 12, 13 y 54.


edades = [45, 56, 32, 14, 78, 34, 12, 13, 54]


Línea 2-4
Estas líneas crean tres listas vacías: "menores_18", "adultos" y "mayores_65". Estas listas se utilizarán para almacenar las edades clasificadas.


menores_18 = []
adultos = []
mayores_65 = []


Línea 5
Esta línea comienza un ciclo for que itera sobre la lista "edades". La variable "edad" toma el valor de cada edad en la lista durante cada iteración.


for edad in edades:


Línea 6-11
Estas líneas evalúan la edad actual y la clasifican en una de las tres categorías: menores de 18, adultos o mayores de 65.


if edad < 18:
    menores_18.append(edad)
elif edad >= 18 and edad < 65:
    adultos.append(edad)
else:
    mayores_65.append(edad)


Línea 12-15
Estas líneas imprimen los resultados, mostrando la lista original de edades y las listas clasificadas.


print("\n La Lista De Edades Es:", edades)
print("\n La Lista De Menores De Edad Es:", menores_18)
print("\n La Lista De Adultos Es:", adultos)
print("\n La Lista De Adultos Mayores a 65:", mayores_65)


Estructuras WHILE

Las estructuras while se ejecutan mientras la condición que se encuentra sea verdadera.

Ejemplo 1: Imprimir los números del 1 al 10


i = 1
while i <= 10:
    print(i)
    i += 1


Ejemplo 2: Imprimir los números del 10 al 1


i = 10
while i >= 1:
    print(i)
    i -= 1
