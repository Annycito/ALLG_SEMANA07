Capacidad_mochila = int(input("Ingrese la capacidad de la mochila: "))
#lista de pesos y precios 
nombres  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
pesos    = [10,  4,   7,   5,   3,   3,   2,   1]
precios  = [4,   3,   3,   2,   1,   2,   1.8, 3]
#buscar la relacion precio/peso
ratios_con_indice = []
for i in range(len(nombres)):
    ratio = precios[i] / pesos[i]
    ratios_con_indice.append((ratio, i))
# ordenar de forma descendente
#examen no LAMBA NO LAMBA, REPITO NO LAMBA 
ratios_con_indice.sort(key=lambda x: x[0], reverse=True)

kg = [0.0] * len(nombres)
restante = Capacidad_mochila
soles = 0.0
print("\n******PROCESO DETALLADO ******")
for ratio, i in ratios_con_indice:
    if restante <= 0:
        break
        
    nombre_caja = nombres[i]
    peso_caja = pesos[i]
    precio_caja = precios[i]
    
    # Si la caja entra completa
    if peso_caja <= restante:
        kg [i] = float(peso_caja)
        soles += precio_caja
        restante -= peso_caja
        print(f"Caja {nombre_caja} ; ({peso_caja}Kg, S/{precio_caja}) >>>>> Espacio restante: {restante:.2f}Kg")
    
    # Para llevar solo una fracción de una caja
    else:
        fraccion = restante / peso_caja
        kg [i] = float(restante)
        soles += fraccion * precio_caja
        print(f"Caja {nombre_caja} pero fraccionada ({restante:.2f}Kg de {peso_caja}Kg) >>>>> Mochila llena (0.00Kg)")
        restante = 0

    #resultado final
print("\n******RESULTADO FINAL******")
print(f"Ganaste: S/{soles:.2f}")
print("Detalle Final resumido:")

for i in range(len(nombres)):
    if kg [i] > 0:
        print(f"- Caja {nombres[i]}: se cargaron {kg [i]:.2f} Kg de {pesos[i]} Kg")