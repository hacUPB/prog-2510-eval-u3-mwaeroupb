## Ejercicio 1

Observa el siguiente ejemplo práctico de un bucle `while` que imprime números del 1 al 5:

```python
numero = 1
while numero <= 5:
    print(numero)
    numero += 1  # numero = numero + 1
```
1. Ejercicio
```python
# Solicitar al usuario el número de términos de la sucesión
N = int(input("Ingrese el número de términos de la sucesión de Fibonacci: "))

# Inicializamos los dos primeros términos de la sucesión
a, b = 0, 1

# Imprimir los primeros N términos de la sucesión de Fibonacci
print("Sucesión de Fibonacci:")
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b  # Actualizamos los valores de a y b
```
2. Ejercicio
```python
# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Inicializar el contador para el bucle while
contador = 1

# Imprimir la tabla de multiplicar del número
print(f"Tabla de multiplicar del {numero}:")
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1  # Incrementamos el contador en cada iteración
```
### Bucle for
# Lista de canciones favoritas
```python
canciones_favoritas = ["Shape of You", "Blinding Lights", "Rolling in the Deep", "Levitating", "Bohemian Rhapsody"]

# Usando el ciclo for para imprimir cada canción en la lista
for cancion in canciones_favoritas:
    print(cancion)
```
### Ejercicio 2: usando la función range()
```python
# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializar la variable suma
suma = 0

# Usar el bucle for con range() para sumar los números pares
for numero in range(2, n+1, 2):  # Empieza en 2, hasta n (inclusive), de 2 en 2
    suma += numero

# Mostrar el resultado de la suma
print(f"La suma de todos los números pares desde 1 hasta {n} es: {suma}")
```
###  Ejercicio 3:
```python
 # Solicitar al usuario que ingrese una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Inicializar una variable para contar la longitud
longitud = 0

# Usar un bucle for para recorrer cada carácter en la cadena
for caracter in cadena:
    longitud += 1  # Aumentar el contador por cada carácter

# Mostrar la longitud de la cadena
print(f"La longitud de la cadena es: {longitud}")
```
### Ejercicio 4:
```python
# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Crear una lista vacía llamada numeros_pares
numeros_pares = []

# Usar un bucle for para agregar los primeros n números pares
for i in range(n):
    # El número par es 2 * (i + 1)
    numeros_pares.append(2 * (i + 1))

# Mostrar la lista de números pares
print("Los primeros", n, "números pares son:", numeros_pares)
```
### Ejericio 5: altitud de vuelo
```python
import random

# Solicitar al usuario cuántos datos de altitud quiere generar
cantidad = int(input("¿Cuántos datos de altitud deseas generar? "))

# Crear una lista vacía para almacenar las altitudes de vuelo
altitudes = []

# Usar un bucle for para generar los datos de altitud
for _ in range(cantidad):
    # Generar un valor aleatorio entre 10000 y 15000 metros
    altitud = random.randint(10000, 15000)
    # Añadir la altitud a la lista
    altitudes.append(altitud)

# Mostrar la lista de altitudes
print("Las altitudes generadas son:", altitudes)

```
### Ejericio 5: altitud de vuelo 6
```python
# Inicializar las variables para acumular las calificaciones y contar cuántas se ingresan
suma_calificaciones = 0
cantidad_calificaciones = 0

# Solicitar la primera calificación
calificacion = float(input("Ingresa una calificación (0 para finalizar): "))

# Verificar si el primer valor ingresado es 0, en cuyo caso mostrar un mensaje de error
if calificacion == 0:
    print("Error: no se puede ingresar 0 como la primera calificación.")
else:
    # Mientras la calificación ingresada no sea 0, seguir pidiendo calificaciones
    while calificacion != 0:
        suma_calificaciones += calificacion  # Sumar la calificación al total
        cantidad_calificaciones += 1  # Contar una calificación más
        
        # Solicitar la siguiente calificación
        calificacion = float(input("Ingresa una calificación (0 para finalizar): "))
    
    # Si al menos una calificación fue ingresada, calcular y mostrar el promedio
    if cantidad_calificaciones > 0:
        promedio = suma_calificaciones / cantidad_calificaciones
        print(f"El promedio de las calificaciones es: {promedio:.2f}")
    else:
        print("No se ingresaron calificaciones válidas.")
```
### Ejercicio 7: Programa de Conversión de Temperatura
```python
# Encabezados de la tabla
print("Celsius | Fahrenheit")
print("---------------------")

# Bucle para generar la tabla
for celsius in range(0, 101, 10):  # Rango de 0 a 100, con un paso de 10
    fahrenheit = (celsius * 9/5) + 32  # Conversión de Celsius a Fahrenheit
    print(f"{celsius:7} | {fahrenheit:10.1f}")  # Imprimir los valores formateados
```