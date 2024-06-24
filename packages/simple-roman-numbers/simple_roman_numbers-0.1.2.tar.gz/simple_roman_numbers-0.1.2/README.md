### README.md

# RomanNumber

`RomanNumber` es una clase en Python que permite convertir entre números enteros y números romanos, además de realizar operaciones aritméticas (suma, resta, multiplicación y división) con ellos.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Métodos](#métodos)
- [Ejemplos](#ejemplos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación

```
pip install simple-roman-number
```

## Uso

### Importar la clase

```python
from simple_roman_number import RomanNumber
```

### Crear una instancia de `RomanNumber`

Puedes crear una instancia de `RomanNumber` utilizando un número entero, un número flotante (se toma solo la parte entera) o una cadena de texto que represente un número romano.

```python
# Usar un número entero
roman_number = RomanNumber(1987)

# Usar un número flotante
roman_number_from_float = RomanNumber(1987.9)

# Usar una cadena de texto con un número romano
roman_number_from_literal = RomanNumber("MCMLXXXVII")
```

### Atributos

- `value`: Propiedad que devuelve el valor entero del número.
- `lit`: Propiedad que devuelve la representación romana del número.

### Operaciones aritméticas

La clase `RomanNumber` soporta las siguientes operaciones aritméticas:
- Suma (`+`)
- Resta (`-`)
- Multiplicación (`*`)
- División (`/`)

## Ejemplos

### Convertir de entero a romano

```python
roman_number = RomanNumber(1987)
print(roman_number.lit)  # Imprime: "MCMLXXXVII"
```

### Convertir de romano a entero

```python
roman_number_from_literal = RomanNumber("MCMLXXXVII")
print(roman_number_from_literal.value)  # Imprime: 1987
```

### Operaciones aritméticas

```python
a = RomanNumber(10)
b = RomanNumber(5)

print(a + b)  # Imprime: "XV" (RomanNumber(15))
print(a - b)  # Imprime: "V" (RomanNumber(5))
print(a * b)  # Imprime: "L" (RomanNumber(50))
print(a / b)  # Imprime: "II" (RomanNumber(2))

# También funciona con números normales
print(a + 5)  # Imprime: "XV" (RomanNumber(15))
print(a - 3)  # Imprime: "VII" (RomanNumber(7))
print(a * 2)  # Imprime: "XX" (RomanNumber(20))
print(a / 2)  # Imprime: "V" (RomanNumber(5))
```

### Imprimir la representación romana

```python
roman_number = RomanNumber(1987)
print(roman_number)  # Imprime: "MCMLXXXVII"
```

