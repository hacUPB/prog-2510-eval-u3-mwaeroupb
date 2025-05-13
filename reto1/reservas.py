
# reservas.py

import random

# 1. Información del usuario
titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print(titulo + " " + nombre + " " + apellido + ", ¡Bienvenido a FastFast Airlines!")

# 2. Selección de vuelo
print("\nCiudades disponibles: Medellín, Bogotá, Cartagena")
origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese la ciudad de destino: ")

# Validar que origen y destino estén en la lista y no sean iguales
if origen == destino:
    print("El origen y el destino no pueden ser iguales.")
    exit()

# Distancias entre ciudades
distancias = {
    ("Medellín", "Bogotá"): 240,
    ("Bogotá", "Medellín"): 240,
    ("Medellín", "Cartagena"): 461,
    ("Cartagena", "Medellín"): 461,
    ("Bogotá", "Cartagena"): 657,
    ("Cartagena", "Bogotá"): 657
}

# Obtener distancia
distancia = distancias.get((origen, destino))
if distancia == None:
    print("Ruta no válida.")
    exit()

dia_semana = input("Ingrese el día de la semana en que desea viajar: ")
dia_mes = int(input("Ingrese el día del mes (1 al 30): "))

# Calcular precio
if distancia < 400:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles" or dia_semana == "jueves":
        precio = 79900
    elif dia_semana == "viernes" or dia_semana == "sabado" or dia_semana == "domingo":
        precio = 119900
    else:
        print("Día inválido.")
        exit()
else:
    if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles" or dia_semana == "jueves":
        precio = 156900
    elif dia_semana == "viernes" or dia_semana == "sabado" or dia_semana == "domingo":
        precio = 213000
    else:
        print("Día inválido.")
        exit()

# 3. Asignación de asiento
preferencia = input("¿Prefiere un asiento en el pasillo, junto a la ventana o sin preferencia?: ")

if preferencia == "pasillo":
    letra_asiento = "C"
elif preferencia == "ventana":
    letra_asiento = "A"
else:
    letra_asiento = "B"

numero_asiento = random.randint(1, 29)
asiento = str(numero_asiento) + letra_asiento

# 4. Mostrar resumen
print("\n--- Confirmación de Reserva ---")
print("Pasajero:", titulo, nombre, apellido)
print("Ruta:", origen, "→", destino)
print("Fecha:", dia_semana, dia_mes)
print("Precio del boleto: $" + str(precio))
print("Asiento asignado:", asiento)



