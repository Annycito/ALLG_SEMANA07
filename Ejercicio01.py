monto = float(input("Ingrese el monto a pagar: "))
#variables
monto_centimos = round(monto * 100)
resultado = {}
#lista
denominacion_monedas = [200, 100, 50, 20, 10, 5, 2, 0.05]
# Recorremos la lista 
for moneda in denominacion_monedas:
    moneda_centimos = round(moneda * 100)
    cantidad = monto_centimos // moneda_centimos
    
    if cantidad > 0:
        resultado[moneda] = cantidad
        monto_centimos %= moneda_centimos

print("\nRespuesta:")
for moneda, cantidad in resultado.items():
    print(f"{cantidad} de S/{moneda:g}")


