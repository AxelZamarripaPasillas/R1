# Un programa Que Cálcule El Nivel De Desempeño De Un Estudiante Respecto Con Su Calificación Dada Por El Estudiante
# Fecha: 20241029
# Elaborado Por: Axel Zamarripa Pasillas.

cal = float(input("¿Cuál Es Tu Calificación Final? "))

if cal <= 60.0:
     print ("Insuficiente")

elif cal  >= 70.0  or  cal < 80.0:
     print ("Suficiente")

elif cal >=80.0 or cal <90.0:
      print ("Muy Bien")

elif cal >=90.0 or cal <96.0:
     print ("Notable")

else:
     cal >=96.0  or cal <= 100.0
     print ("Excelente")

print ("¡Gracias Por Usar Nuestro Programa!")
