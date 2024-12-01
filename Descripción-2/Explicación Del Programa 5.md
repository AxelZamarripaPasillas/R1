## PROGRAMA DE COMPARACIONES CON "STRING"
En este programa, se muestra cómo realizar comparaciones con cadenas de texto utilizando operadores de comparación y de membresía.

### Explicación Del Programa:
### COMPARACIONES:
#### Línea 6: 
print ("perro" == "perro") # True

Esta línea utiliza el operador == para comparar si las cadenas de texto "perro" y "perro" son iguales. El resultado es True porque las cadenas son idénticas.

#### Línea 7: 
print ("perro" != "gato") # True

Esta línea utiliza el operador != para comparar si las cadenas de texto "perro" y "gato" son diferentes. El resultado es True porque las cadenas son diferentes.

#### Línea 8: 
print ("Aguascalientes" < "Zacatecas") # False

Esta línea utiliza el operador < para comparar si la cadena de texto "Aguascalientes" es menor que la cadena de texto "Zacatecas". El resultado es False porque la cadena "Aguascalientes" es mayor que la cadena "Zacatecas" en orden alfabético.

#### Línea 9: 
print ("Aire" >= "Agua") #

Esta línea utiliza el operador >= para comparar si la cadena de texto "Aire" es mayor o igual que la cadena de texto "Agua". El resultado no se muestra en el código, pero sería True porque la cadena "Aire" es mayor que la cadena "Agua" en orden alfabético.

### MEMBERSHIP:
#### Línea 14: 
print ("house" in "boathouse") #True

Esta línea utiliza el operador in para verificar si la cadena de texto "house" se encuentra dentro de la cadena de texto "boathouse". El resultado es True porque la cadena "house" es una subcadena de la cadena "boathouse".

#### Línea 15: 
print ("bien" in "bienvenidos") #True

Esta línea utiliza el operador in para verificar si la cadena de texto "bien" se encuentra dentro de la cadena de texto "bienvenidos". El resultado es True porque la cadena "bien" es una subcadena de la cadena "bienvenidos".

#### Línea 16: 
print ("y" not in "ejes") #True

Esta línea utiliza el operador not in para verificar si la cadena de texto "y" no se encuentra dentro de la cadena de texto "ejes". El resultado es True porque la cadena "y" no es una subcadena de la cadena "ejes".

#### Línea 17: 
print ("je" not in "ejes") #False

Esta línea utiliza el operador not in para verificar si la cadena de texto "je" no se encuentra dentro de la cadena de texto "ejes". El resultado es False porque la cadena "je" es una subcadena de la cadena "ejes".

### SLICING (REBANADOR):
#### Línea 21: 
mi_nombre = "Choto Chorchis"

Esta línea asigna la cadena de texto "Choto Chorchis" a la variable mi_nombre.

#### Línea 22: 
print (mi_nombre [3])

Esta línea utiliza el índice 3 para acceder al cuarto carácter de la cadena de texto mi_nombre. El resultado es el carácter "t".

#### Línea 23: 
print (mi_nombre [12])

Esta línea utiliza el índice 12 para acceder al decimotercer carácter de la cadena de texto mi_nombre. El resultado es el carácter "s".

#### Línea 26: 
mi_nombre = "JOSÉ LUIS"

Esta línea asigna la cadena de texto "JOSÉ LUIS" a la variable mi_nombre.

#### Línea 27: 
print (mi_nombre [2:6])

Esta línea utiliza el índice 2:6 para acceder a los caracteres desde el tercer carácter hasta el sexto carácter de la cadena de texto mi_nombre. El resultado es la cadena de texto "SÉ L".
