# Rentabilidad 
# utilidad = precio suscripcion * numero de usuarios - gastos totales

print("Calcule la rentabilidad de su emprendimiento ")
precio_suscripcion = float(input("Ingrese el precio de la suscripcion mensual en pesos: $"))
numero_usuarios = int(input("Ingrese el numero de usuarios por mes (ejemplo: 15)  :"))
gastos_totales = float(input("Ingrese los gastos totales por mes en pesos : $"))

utilidad = round((precio_suscripcion * numero_usuarios) - gastos_totales,2)

print(f"La utilidad mensual de su empredimiento es ${utilidad}")