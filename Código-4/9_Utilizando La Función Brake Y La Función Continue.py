i = 1
while i <=10:
    if i == 5:
        break
    print (i)
    i += 1 # Equivale a i = i +1
print ("Fin Del Programa")

# Ejemplo 2 - Continue
# Imprimir los numeros del 1 al 10,
# pero si el número es 5, omitirlo
i = 1
while i <= 10:
    if i == 5:
        1 += 1
        continue
    print (i)
    i += 1
print ("Fin Del Programa")
