#The Sum Pattern
numeros = [100, 200, 300, 400]
sumatoria = 0 #inicialización

for numero in numeros:
    sumatoria = sumatoria + numero 
print ("La Sumatoria Es", sumatoria)

#The Accumulation Pattern
palabras = ["Hoy", " ", "Hace", " ", "Frío"]
mensaje = ""
for palabra in palabras:
    mensaje = mensaje + palabra
print (mensaje)

#THE MAP PATTERN
#Sirve para "mapear" cad uno de los elementos en una nueva variable. Por ejemplo, para crear una lista idéntica nueva desde otra que ya existente.

lista_anterior = ["Manzana", "Piña", "Uva"]
lista_nueva = []
print ("La Lista Vacía", lista_nueva)
for fruta in lista.anterior:
    lista_nueva.append (fruta)
    print ("La Lista Copiada es", lista_nueva)
