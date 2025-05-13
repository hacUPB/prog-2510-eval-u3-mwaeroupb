# Solucion de ejercicios: 

### Ejercicio 1:
Comprueba en la consola de Python los siguientes códigos
```python
print(10 > 5)
print("Hola" != "Mundo")
print(3.14 <= 4.5)
nombre = "Juan"
print(nombre == "Juan")
```
### Ejercicio 2

#### Enunciado:
Un almacén cobra `$9 000` por costos de envío, pero ofrece el **envío gratis** para compras superiores a `$100 000`. En caso contrario, se debe pagar el costo de envío.  
Solicita al usuario el valor de la compra y calcula el valor total a pagar.

#### Solución en Python:

```python
compra = float(input("Ingrese el valor de su compra: "))

if compra > 100000:
    total = compra
    print("¡Envío gratis!")
else:
    total = compra + 9000
    print("Costo de envío: $9000")

print(f"Total a pagar: ${total}")
```
### Ejercicio 3

#### Enunciado:
Solicita al usuario un número y determina si es **par** o **impar**.

#### Solución en Python:

```python
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.") 
```
### Ejercicio 4

#### 🔹 Propuesta 1: Condicional Simple

**Enunciado:**  
Una cafetería ofrece un descuento del 10% si el cliente compra más de 3 cafés.  
Solicita al usuario la cantidad de cafés que desea comprar y muestra si tiene o no derecho al descuento.

**Sugerencia de solución:**

```python
cantidad = int(input("¿Cuántos cafés desea comprar?"))

if cantidad > 3:
    print("¡Tienes un 10% de descuento en tu compra!")
```
### Ejercicio 5

#### Enunciado:
El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, con el fin de identificar su vulnerabilidad.  
Diseña un algoritmo que pida al usuario su edad y la clasifique en la etapa correspondiente.  
**Importante:** Verificar que no se ingresen valores menores a cero.

#### Clasificación etaria:

- **Primera Infancia** (0 - 5 años)
- **Infancia** (6 - 11 años)
- **Adolescencia** (12 - 18 años)
- **Juventud** (14 - 26 años)
- **Adultez** (27 - 59 años)
- **Persona Mayor** (60 años o más)

#### Solución en Python:

```python
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error: la edad no puede ser negativa.")
else:
    if 0 <= edad <= 5:
        print("Primera Infancia")
    elif 6 <= edad <= 11:
        print("Infancia")
    elif 12 <= edad <= 18:
        print("Adolescencia")
    elif 14 <= edad <= 26:
        print("Juventud")
    elif 27 <= edad <= 59:
        print("Adultez")
    else:
        print("Persona Mayor (Envejecimiento y vejez)")
```
### Ejercicio 6

#### Enunciado:
Una compañía de paquetería internacional opera en diferentes zonas y su costo depende del peso del paquete y la zona de destino.  
**Condiciones:**
- No se transportan paquetes de más de 5 kg.
- El costo por gramo varía según la zona:

| Zona | Ubicación          | Costo/gramo |
|-----|--------------------|------------|
| 1   | América del Norte   | $11        |
| 2   | América Central     | $10        |
| 3   | América del Sur     | $12        |
| 4   | Europa              | $24        |
| 5   | Asia                | $27        |

#### Solución en Python:

```python
peso = float(input("Ingrese el peso del paquete en kilogramos: "))
zona = int(input("Ingrese la zona de destino (1-5): "))

if peso > 5:
    print("Lo sentimos, no transportamos paquetes que pesen más de 5 kg.")
else:
    peso_gramos = peso * 1000

    if zona == 1:
        costo = peso_gramos * 11
        destino = "América del Norte"
    elif zona == 2:
        costo = peso_gramos * 10
        destino = "América Central"
    elif zona == 3:
        costo = peso_gramos * 12
        destino = "América del Sur"
    elif zona == 4:
        costo = peso_gramos * 24
        destino = "Europa"
    elif zona == 5:
        costo = peso_gramos * 27
        destino = "Asia"
    else:
        print("Zona inválida.")
        costo = None

    if costo is not None:
        print(f"El costo de envío a {destino} es: ${costo}")
```
### Ejercicios para practicar

---

#### 1. Menú de Operaciones Aritméticas

Crear un menú donde el usuario pueda elegir entre las cinco operaciones aritméticas básicas: `+`, `-`, `*`, `/`, `%`.

```python
print("Seleccione la operación que desea realizar:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
print("5. Módulo (%)")

opcion = int(input("Ingrese una opción (1-5): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    print(f"Resultado: {num1 + num2}")
elif opcion == 2:
    print(f"Resultado: {num1 - num2}")
elif opcion == 3:
    print(f"Resultado: {num1 * num2}")
elif opcion == 4:
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Error: División entre cero no permitida.")
elif opcion == 5:
    if num2 != 0:
        print(f"Resultado: {num1 % num2}")
    else:
        print("Error: División entre cero no permitida.")
else:
    print("Opción inválida.")
```
### 2. Día de la semana según número
```python
numero = int(input("Ingrese un número entre 1 y 7: "))

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if 1 <= numero <= 7:
    print(f"El día correspondiente es: {dias[numero]}")
else:
    print("Número inválido. Debe ser entre 1 y 7.")
```
### 3. Consumo de combustible con margen de seguridad
```python

distancia = float(input("Ingrese la distancia del vuelo en kilómetros: "))
consumo_por_km = float(input("Ingrese el consumo de combustible por kilómetro: "))

combustible_requerido = distancia * consumo_por_km

if distancia <= 1000:
    combustible_requerido *= 1.10  # Añade 10%
else:
    combustible_requerido *= 1.15  # Añade 15%

print(f"La carga total de combustible requerida es: {combustible_requerido:.2f} litros")
```
## 9. Ejercicio Propuesto

### Menú Repetitivo

**Instrucciones:**
- Crear un menú de opciones (1: "Sumar", 2: "Restar", 3: "Salir").
- Utilizar `while True:` para **mantener** el menú **hasta** que el usuario elija "Salir".
- Emplear `match-case` (o `if-elif-else` si no tienes Python 3.10+) para gestionar cada opción.

---

### Código (con `match-case`, Python 3.10+)

```python
while True:
    print("\nMenú de Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La suma es: {num1 + num2}")
        case "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La resta es: {num1 - num2}")
        case "3":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
```
