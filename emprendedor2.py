# Rentabilidad 
# utilidad = precio suscripcion * numero de usuarios - gastos totales

print("Calcule la rentabilidad de su emprendimiento ")
precio_suscripcion = float(input("Ingrese el precio de la suscripcion mensual en pesos: $"))
numero_usuarios_normales = int(input("Ingrese el numero de usuarios normales por mes (ejemplo: 100) : "))
numero_usuarios_premium = int(input("Ingrese el numero de usuarios premium por mes (ejemplo: 25) :"))
gastos_totales = float(input("Ingrese los gastos totales por mes en pesos: $"))

utilidad = round((precio_suscripcion * numero_usuarios_normales) + (precio_suscripcion * 1.5 * numero_usuarios_premium ) - gastos_totales,2)

print(f"La utilidad mensual de su empredimiento es ${utilidad}")