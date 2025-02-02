"""
Este módulo calcula estadísticas descriptivas 
(media, mediana, moda, varianza, desviación estándar)
a partir de un archivo de texto con números.
"""

import sys
import time

def read_numbers(file_path):
    """Lee un archivo y devuelve una lista de números válidos."""
    values = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    values.append(float(line.strip()))
                except ValueError:
                    print(f"Ignorando valor no numérico: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        sys.exit(1)
    return values

def mean(numbers):
    """Calcula la media de una lista de números."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calcula la mediana de una lista de números."""
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    return numbers[n//2]

def mode(numbers):
    """Calcula la moda de una lista de números."""
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    highest_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == highest_freq]
    return modes if len(modes) < len(numbers) else None

def variance(numbers, mean_value):
    """Calcula la varianza de una lista de números."""
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def stddev(variance_value):
    """Calcula la desviación estándar a partir de la varianza."""
    return variance_value ** 0.5

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py archivo_datos.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    data_values = read_numbers(input_file)

    if not data_values:
        print("Error: No hay números válidos en el archivo.")
        sys.exit(1)

    avg_value = mean(data_values)
    med_value = median(data_values)
    mod_value = mode(data_values)
    var_value = variance(data_values, avg_value)
    std_value = stddev(var_value)

    elapsed_time = time.time() - start_time

    results = f"""
    Estadísticas calculadas:
    - Media: {avg_value}
    - Mediana: {med_value}
    - Moda: {mod_value}
    - Varianza: {var_value}
    - Desviación estándar: {std_value}
    - Tiempo de ejecución: {elapsed_time:.5f} segundos
    """

    print(results)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(results)
