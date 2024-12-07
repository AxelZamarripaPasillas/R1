edades = [45, 56, 32, 14, 78, 34, 12, 13, 54]
menores_18 = [] #Lista vacía para menores de 18
adultos = [] # lista vacía para adultos entre 18 y 64
mayores_65 = [] #Lista vacía para mayores de 65

for edad in edades: 
    if edad <18:
        menores_18.append (edad)
    elif edad >= 18 and edad < 65:
        adultos.append (edad)
    else:
        mayores_65.append (edad)

#-----Imprimir Los Resultados
print ("\n \u286 La Lista De Edades Es:", edades)
print ("\n \u286 La Lista De Menores De Edad Es:", menores_18)
print ("\n \u286 La Lista De Adultos Es:", adultos)
print ("\n \u286 La Lista De Adultos Mayores a 65:",mayores_65)

"""""Las Estructuras WHILE Se Ejecutan Mientras La Condición 
Que Se Encuentra Sea Verdadera."""

#Ejemplo 1
#Impime Los Numeros Del 1 al 10
i = 1 #Inicialización De La Variable De Control
while i <= 10: #Condición de parada
    print (i)
    i+=1 #Equivalente a i= i +1

#Sintaxis:
#while <condición>:
# <cuerpo del while>

#Ejemplo 2
#Imprimir los numeros del 10 al 1
i = 10
while i >= 1:
    print (i)
i -= 1
