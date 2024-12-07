numeros = [10, 50, 25, 13, 10, 28, 100, 500, 29, 27]
menores_50 = [] #Crea una lista vacía 

for numero in numeros:
    if numero < 50:
        menores_50.append (numero)

print ("La Lista Original Es:", numeros)
print ("La Nueva Lista Es:", menores_50)
