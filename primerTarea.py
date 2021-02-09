print("Bienvenido al programa")
#Datos con su tipo de datos
velocidadcoche = 80
presupuestocoche = 500
precioxlitro = float(input("Cuanto cuesta el litro de gasolina?"))
rendimiento = float(input("Cuanto rinde por litro el coche? "))

#Operaciones a realizar
litrosdisponibles = presupuestocoche / precioxlitro
distancia = litrosdisponibles * rendimiento
tiempo = velocidadcoche / distancia
horas = int(tiempo)
minutos = int((tiempo - horas)*60)

    #Resultados a mostrar
print("Con ", presupuestocoche, "pesos")
print("Se recorren: ", distancia, "km/h")
print("En ", horas, " Horas ", minutos, " minutos")