# CONDICIONAL IF
# Fecha:20241024.
# Elaborado Por: Axel Zamarripa Pasillas.

calificacion_1 = float(input("Ingresa La Calificación De La Unidad 1: "))
calificacion_2 = float(input("Ingresa La Calificación De La Unidad 2: "))
calificacion_3 = float(input("Ingresa La Calificación De La Unidad 3: "))
calificacion_4 = float(input("Ingresa La Calificación De La Unidad 4: "))
calificacion_5 = float(input("Ingresa La Calificación De La Unidad 5: "))
calificacion_6 = float(input("Ingresa La Calificación De La Unidad 6: "))

calificacion_final = (calificacion_1 + calificacion_2 + calificacion_3 + calificacion_4 + calificacion_5 + calificacion_6)/6

print ("Tu Promedio Final Es: ", calificacion_final)

if calificacion_final >= 70:
    print ("Aprobaste")

else:
    print ("Reprobaste")
