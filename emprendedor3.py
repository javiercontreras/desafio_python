# Rentabilidad 
# utilidad = precio suscripcion * numero de usuarios - gastos totales

print("Calcule la rentabilidad de su emprendimiento y la razon entre utilidades con respecto al periodo anterior ")
precio_suscripcion = float(input("Ingrese el precio de la suscripcion anual en pesos: $"))
numero_usuarios_normales = int(input("Ingrese el numero de usuarios normales anuales :"))
gastos_totales = float(input("Ingrese los gastos totales anuales en pesos: $"))

utilidad = (precio_suscripcion * numero_usuarios_normales) - gastos_totales
 
print(f"La utilidad anual de su empredimiento es ${utilidad}")
utilidad_periodo_anterior = float(input("Ingrese la utilidad del periodo anterior en pesos : $"))
razon_utilidad =  (utilidad/utilidad_periodo_anterior)

print(f"La razon entre la utilidad de este periodo y el anterior es : {razon_utilidad:.2f} ")