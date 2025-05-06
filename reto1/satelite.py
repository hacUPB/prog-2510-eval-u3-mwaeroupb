# Solicitar datos de entrada al usuario
altitud_inicial = float(input("Ingresa la altitud inicial del satélite (en km): "))
coeficiente_arrastre = float(input("Ingresa el coeficiente de arrastre inicial: "))
altitud_minima = float(input("Ingresa la altitud mínima de seguridad (en km): "))

# Inicializar las variables
altitud_actual = altitud_inicial
numero_orbitas = 0

# Iniciar la simulación de la desintegración orbital
while altitud_actual > altitud_minima:
    # Calcular la pérdida de altitud debido al arrastre
    altitud_perdida = coeficiente_arrastre * altitud_actual
    altitud_actual -= altitud_perdida
    
    # Aumentar el coeficiente de arrastre debido a la disminución de altitud
    coeficiente_arrastre += 0.0001
    
    # Aumentar el contador de órbitas
    numero_orbitas += 1
    
    # Si la pérdida de altitud es muy pequeña, el satélite se estabiliza
    if altitud_perdida < 0.0001:
        print(f"El satélite se ha estabilizado en órbita a una altitud de {altitud_actual:.2f} km.")
        print(f"Número de órbitas completadas: {numero_orbitas}")
        break
else:
    # Si el satélite llega a la altitud mínima de seguridad
    print(f"El satélite ha reingresado a la atmósfera a una altitud de {altitud_actual:.2f} km.")
    print(f"Número total de órbitas completadas: {numero_orbitas}")
