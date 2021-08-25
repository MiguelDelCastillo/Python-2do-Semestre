from collections import namedtuple

Punto = namedtuple("Punto","x y") # Crea la clase ya especializada

punto = Punto(10, 20) # Crea la instancia que representa a un punto en especifico
pass

print(f"Ubicacion del punto, sobre el eje x = {punto.x}")

print(f"Ubicacion del punto, sobre el eje y = {punto.y}")

# Variaciones respecto a la cracion de tuplas nominadas

Persona = namedtuple("Persona",
                     ("nombre","primer_apellido","segundo_apellido"),
                     defaults = ["NA"])

mi_persona = Persona("Miguel","del Castillo")
print("\n")
print(f"Mi nombre es: {mi_persona.nombre}")
print(f"Mi primer apellido es: {mi_persona.primer_apellido}")
print(f"Mi segundo apellido es: {mi_persona.segundo_apellido}")