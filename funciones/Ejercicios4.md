# Ejercicios
### Ejercicio 1
Abre la consola de Python y ejecuta el siguiente comando:
```python
institucion = "Universidad Pontificia Bolivariana"
type(institucion)
 ```
 ## Ejercicio 2

- **Función vs Método**:  
  Una **función** es independiente (`print()`), un **método** pertenece a un objeto (`texto.upper()`).

- **5 funciones propias de Python**:  
  `print()`, `len()`, `type()`, `int()`, `input()`

- **¿Para qué sirve `dir()`?**  
  Muestra una lista de métodos y atributos que tiene un objeto.

- **¿Cómo se llaman las variables dentro de los paréntesis al llamar una función?**  
  Se llaman **argumentos**.

- **¿Diferencia entre argumentos y parámetros?**  
  - **Parámetros**: se definen al crear la función.  
  - **Argumentos**: se pasan al llamar la función.

## Ejercicio 4: Error en llamada de función

### 🧾 Error observado

```python
division()
```
Este código genera el error:
```python
TypeError: division() missing 2 required positional arguments: 'Num1' and 'Num2'
```
## Ejercicio 5

Resuelve los siguientes ejercicios con lo aprendido en la clase de hoy:

### **Problema 1: Conversión de Puntuación**
```python
def convertir_puntuacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"
    elif puntuacion >= 90:
        return "A"
    elif puntuacion >= 80:
        return "B"
    elif puntuacion >= 70:
        return "C"
    elif puntuacion >= 60:
        return "D"
    else:
        return "F"

# Ejemplos de uso
print(convertir_puntuacion(95))  # A
print(convertir_puntuacion(82))  # B
print(convertir_puntuacion(73))  # C
print(convertir_puntuacion(65))  # D
print(convertir_puntuacion(50))  # F
print(convertir_puntuacion(-5))  # Puntuación inválida
```
### **Problema 2: Determinar el Día de la Semana**
```python
def determinar_dia(numero_dia):
    if numero_dia == 1:
        return "Lunes"
    elif numero_dia == 2:
        return "Martes"
    elif numero_dia == 3:
        return "Miércoles"
    elif numero_dia == 4:
        return "Jueves"
    elif numero_dia == 5:
        return "Viernes"
    elif numero_dia == 6:
        return "Sábado"
    elif numero_dia == 7:
        return "Domingo"
    else:
        return "Número de día inválido"

# Ejemplos de uso
print(determinar_dia(1))  # Lunes
print(determinar_dia(4))  # Jueves
print(determinar_dia(7))  # Domingo
print(determinar_dia(0))  # Número de día inválido
print(determinar_dia(8))  # Número de día inválido
```
## Ejercicio 6
```python
**Explorar Métodos**: Ahora, puedes explorar varios métodos de cadenas. Algunos ejemplos comunes incluyen:

### Cadena base para los ejemplos
texto = "  Hola Mundo Python  "

### .upper(): convierte a mayúsculas
print(texto.upper())  # "  HOLA MUNDO PYTHON  "

### .lower(): convierte a minúsculas
print(texto.lower())  # "  hola mundo python  "

### .replace(): reemplaza "Mundo" por "Universo"
print(texto.replace("Mundo", "Universo"))  # "  Hola Universo Python  "

### .split(): divide la cadena por espacios
print(texto.split())  # ['Hola', 'Mundo', 'Python']

### .strip(): elimina espacios al principio y final
print(texto.strip())  # "Hola Mundo Python"
```