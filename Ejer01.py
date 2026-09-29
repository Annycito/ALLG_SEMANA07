monto = float(input("Ingrese el monto del vuelto: "))
# variable
monto_centimos = round(monto * 100)
resultado = {}
# lista COMPLETA 
denominacion_monedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]

print("\n******PROCESO DE VUELTO******")

# Recorremos la lista e ir restando ciclo por ciclo
for moneda in denominacion_monedas:
    moneda_centimos = round(moneda * 100)
    cantidad = monto_centimos // moneda_centimos
    
    if cantidad > 0:
        resultado[moneda] = cantidad
        # Restamos del monto total
        monto_centimos %= moneda_centimos
        
        # Mostramos lo que se usó y cuánto queda en este ciclo exacto
        print(f"Usaste {cantidad} de S/{moneda:g} **** Restante actual: {monto_centimos / 100:.2f}")

#respuetsa rapida
print("\nRespuesta:")
for moneda, cantidad in resultado.items():
    print(f"{cantidad} de S/{moneda:g}")

