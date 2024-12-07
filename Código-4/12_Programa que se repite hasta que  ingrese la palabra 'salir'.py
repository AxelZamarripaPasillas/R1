# Inicialización de variables
palabra = ""
while palabra != "salir" :
    palabra = input ("Ingresar Una Palabra o 'salir' Para Terminar:")
    palabra = palabra.lower () # Convierte la palabra en mínusculas
    print ("Usted Ingreso:", palabra)
    if palabra == "salir":
        break
    
    print ("Fin Del Programa \U0001F601 \n\n") #Imprime un emoji feliz
    print ("¡Hasta Luego! \U0001F448 \n") #Imprime un emoji de saludo
