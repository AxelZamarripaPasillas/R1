cantidad = int (input("¿Cuántos Artículos Compró?"))

if cantidad >3:
    total= cantidad * 30
else:
    total = cantidad * 45

print ("El Total a Pagar Es $" + str(total))
print("Saludo...")
