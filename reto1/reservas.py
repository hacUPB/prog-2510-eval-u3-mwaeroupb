# 1. Datos del cliente
titulo = input("Ingrese su titulo(sr. o sra.): ")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = titulo + " " + nombre + " " + apellido 
print(nombre_completo + ", ¡Bienvenido a MW Airlines!")

# 2. Seleccion del vuelo
print("Los vuelos disponibles en este momento son: Medellin, Monteria, Bogota.")
origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese su ciudad de destino: ")

while origen == destino:
    print("Error, la ciudad de origen y destino son iguales.")
    destino = input("Ingrese una ciudad de destino diferenete: ")

dia = input("ingrese el dia de su vuelo: ").lower()
fecha= int(input("ingrese el dia del mes en el que desea viajar (1-30): "))

# 3. Distancias entre ciudades
distancia = 0
if (origen == "Medellin" and destino == "Bogota") or (origen == "Bogota" and destino == "Medellin") :
    distancia = distancia +  240 
elif (origen == "Monteria" and destino == "Bogota") or (origen == "Bogota"  and destino == "Monteria"):
    distancia = distancia + 494
elif (origen == "Medellin" and destino == "Monteria") or (origen == "Monteria" and destino == "Medellin"):
    distancia = distancia +  299

# 4. Precios según día y distancia
precio = 0
if distancia < 400:
    if dia == "lunes" or dia== "martes" or dia == "miercoles" or dia == "jueves":
        precio = precio + 79900
    else:
        precio = 119900   




