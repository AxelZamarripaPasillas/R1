# Programa Que Calcule Los Impuestos Que Debe Pagar Un Empleado 
# Fecha: 20241029
# Elaborado Por: Axel Zamarripa Pasillas.

ingresos = float(input("¿Cuáles Son Tus Ingresos? "))

if ingresos <= 1000.0:
    impuestos = ingresos * 0.05

elif ingresos > 1000.0 and ingresos <= 2500:
   impuestos = ingresos * 0.08

elif ingresos > 2500.0 and ingresos <= 6000:
    impuestos = ingresos * 0.12

else:
   impuestos = ingresos * 0.15
    
salario_total = (ingresos - impuestos)

print ("Tus Impuestos Son:" + str(impuestos) + " y Tu Salario Final Es " + str(salario_total)) 
   




