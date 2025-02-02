"""
Este módulo calcula estadísticas descriptivas 
(media, mediana, moda, varianza, desviación estándar)
a partir de un archivo de texto con números.
"""

import sys
import time

def read_numbers(file_name):
    """Lee un archivo y devuelve una lista de números válidos."""
    numbers = []
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Ignorando valor no numérico: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: El archivo '{file_name}' no existe.")
        sys.exit(1)
    return numbers

def mean(nums):
    """Calcula la media de una lista de números."""
    return sum(nums) / len(nums)

def median(nums):
    """Calcula la mediana de una lista de números."""
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2 - 1] + nums[n//2]) / 2
    return nums[n//2]

def mode(nums):
    """Calcula la moda de una lista de números."""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    highest_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == highest_freq]
    return modes if len(modes) < len(nums) else None

def variance(nums, avg):
    """Calcula la varianza de una lista de números."""
    return sum((x - avg) ** 2 for x in nums) / len(nums)

def stddev(var):
    """Calcula la desviación estándar a partir de la varianza."""
    return var ** 0.5

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py archivo_datos.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers(file_name)

    if not numbers:
        print("Error: No hay números válidos en el archivo.")
        sys.exit(1)

    avg = mean(numbers)
    med = median(numbers)
    mod = mode(numbers)
    var = variance(numbers, avg)
    std = stddev(var)

    elapsed_time = time.time() - start_time

    results = f"""
    Estadísticas calculadas:
    - Media: {avg}
    - Mediana: {med}
    - Moda: {mod}
    - Varianza: {var}
    - Desviación estándar: {std}
    - Tiempo de ejecución: {elapsed_time:.5f} segundos
    """

    print(results)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(results)
