# Solucion de ejercicios: 

### Ejercicio 1:
**¿Cuál es el rango de datos que se puede representar con 32 bits?**
Sabemos que:

- Cada bit puede tener dos estados: `0` o `1`.
- Entonces, con **32 bits** se pueden representar \( 2^{32} \) combinaciones diferentes.

Calculamos:

\[
2^{32} = 4,294,967,296
\]

### Ejercicio 2:
#### Operaciones Matemáticas

```python
suma = 2 + 3
multiplicacion = 10 * 5
division = 15 / 3
```
# Para imprimir los resultados:
print(suma)           # Resultado: 5
print(multiplicacion) # Resultado: 50
print(division)       # Resultado: 5.0

#### Cadenas de caracteres
concatenacion = "Hola" + " " + "Mundo"
repeticion = "Python" * 3

#### Para imprimir los resultados:
print(concatenacion)  # Resultado: Hola Mundo
print(repeticion)     # Resultado: PythonPythonPython

#### Listas 
numeros = [1, 2, 3, 4, 5]
porcion = numeros[1:4]

# Para imprimir los resultados:
print(porcion)        # Resultado: [2, 3, 4]

#### Bucles
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

### Ejercicio 3:
Intenta explicar cuál es el error de sintaxis que aparece en la figura 10. Luego corrígelo para que se pueda imprimir correctamente la frase: Yo le dije: “cómo estás?”

El error ocurre porque se están utilizando comillas dobles (") dentro de otras comillas dobles, lo que confunde a Python.

### Ejercicio 4:

#### Uso de Variables en la Función `print()`
```
```python
nombre = "Ana"
edad = 25

# Usando concatenación
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

# Usando f-strings (recomendado en Python 3.6+)
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")