"""
Este programa convierte números de un archivo de texto a binario y hexadecimal
sin usar las funciones predefinidas bin() y hex().
"""

import sys
import time

def read_numbers(file_path):
    """Lee un archivo y devuelve una lista de números enteros válidos."""
    values = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    values.append(int(line.strip()))
                except ValueError:
                    print(f"Ignorando valor no numérico: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        sys.exit(1)
    return values

def to_binary(number):
    """Convierte un número decimal a binario sin usar bin()."""
    binary_str = ""
    while number > 0:
        binary_str = str(number % 2) + binary_str
        number //= 2
    return binary_str if binary_str else "0"

def to_hexadecimal(number):
    """Convierte un número decimal a hexadecimal sin usar hex()."""
    hex_chars = "0123456789ABCDEF"  # Ahora en snake_case
    hex_str = ""
    while number > 0:
        hex_str = hex_chars[number % 16] + hex_str
        number //= 16
    return hex_str if hex_str else "0"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py archivo_numeros.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers(input_file)

    if not numbers:
        print("Error: No hay números válidos en el archivo.")
        sys.exit(1)

    results = []
    for num in numbers:
        BINARY_REP = to_binary(num)  # Ahora en UPPER_CASE
        HEX_REP = to_hexadecimal(num)  # Ahora en UPPER_CASE
        results.append(f"Número: {num} | Binario: {BINARY_REP} | Hexadecimal: {HEX_REP}")

    elapsed_time = time.time() - start_time

    print("\n".join(results))
    print(f"\nTiempo de ejecución: {elapsed_time:.5f} segundos")

    with open("ConversionResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write("\n".join(results))
        result_file.write(f"\nTiempo de ejecución: {elapsed_time:.5f} segundos")
