#1 - Implementar una funcion que tome como argumento una fecha de nacimiento
#    y retorne la edad en años CUMPLIDOS para este dato

#2 - Aplicar mediante la funcion map() la funcion para el calculo de la edad
#    recien codificada en el paso 1 sobre una secuencia de fechas de nacimiento (min 4)
#    Desplegar el resultado de la funcion map, un dato por renglon a la vez
import datetime

fechasNacimiento = ('26/06/2003','25/01/2002','29/05/2000','30/07/2001')
print(fechasNacimiento)
def fecha(valor):
    #Codigo Francisco
    fecha_procesada = datetime.datetime.strptime(valor, "%d/%m/%Y").date()
    fecha_actual = datetime.date.today()
    edad = fecha_actual.year - fecha_procesada.year - ((fecha_actual.month, fecha_actual.day) <= (fecha_procesada.month, fecha_procesada.day))
    return edad

#Boceto V1
aniosCumplidos = list(map(fecha, fechasNacimiento))
print("La edad de cada persona es :")
for i in aniosCumplidos:
    print(i)


