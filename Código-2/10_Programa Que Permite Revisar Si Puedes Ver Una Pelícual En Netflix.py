# PROGRAMA QUE PERIMITE REVISAR SI PUEDES VER UNA PELÍCULA EN NETFLIX
# FECHA:20241025
# NOMBRE: Axel Zamarripa Pasillas.

# Solución 1. If Anidados
edad = int(input("¿Cuántos Años Tienes"))
comprar= int(input("¿Compraste La Película? \n0-NO\n1-SI\n"))
                   
if edad >=18:
   if comprar == 1:
      print("Puede Ver La Película")

else:
     print("Vete a Hacer La Tarea")

print("¡Gracias Por Usar Netflix!")

# Solución 2. Con Compuertas.

edad = int(input("¿Cuántos Años Tienes? "))
comprar = input ("¿Compraste La Película? \n0-NO\n1-SI\n")

puede_ver_pelicula = edad >=18 and comprar

if puede_ver_pelicula: print ("Puedes Ver La Película")
else: print ("No Puedes Ver La Película")

print ("¡Garcias Por Usar Netflix!")

