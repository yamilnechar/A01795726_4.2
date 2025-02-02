"""
Este programa cuenta la frecuencia de palabras en un archivo de texto,
ignorando la puntuación y sin distinguir entre mayúsculas y minúsculas.
"""

import sys
import time
import re

def leer_texto(file_path):
    """Lee un archivo de texto y devuelve una lista de palabras limpias."""
    words = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                # Eliminar signos de puntuación usando regex
                clean_line = re.sub(r'[^\w\s]', '', line.lower())
                words.extend(clean_line.split())
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
        sys.exit(1)
    return words

def contar_palabras(word_list):
    """Cuenta la frecuencia de cada palabra en la lista."""
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count.py archivo_texto.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    words = leer_texto(input_file)

    if not words:
        print("Error: No hay palabras en el archivo.")
        sys.exit(1)

    word_count = contar_palabras(words)
    sorted_results = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    elapsed_time = time.time() - start_time

    # Mostrar resultados en la terminal
    for word, count in sorted_results:
        print(f"{word}: {count}")

    print(f"\nTiempo de ejecución: {elapsed_time:.5f} segundos")

    # Guardar los resultados en un archivo
    with open("WordCountResults.txt", "w", encoding="utf-8") as result_file:
        for word, count in sorted_results:
            result_file.write(f"{word}: {count}\n")
        result_file.write(f"\nTiempo de ejecución: {elapsed_time:.5f} segundos")
