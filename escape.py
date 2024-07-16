import math as ma
print("La velocidad de escape de un planeta se define como la mínima velocidad necesaria para salir de un planeta venciendo la gravedad.")
radio = float(input("Ingrese el radio del planeta en kilometros : ")) * 1000
g = float(input("Ingrese la aceleracion de gravedad del planeta en [m/s^2]  : "))
ve = round((ma.sqrt(2*g * radio)),1)
print(f"La velocidad de escape para un planeta de radio {radio/1000} [km] y una aceleracion de gravedad {g} [m/s^2] es : {ve} [m/s]")
print("\n")