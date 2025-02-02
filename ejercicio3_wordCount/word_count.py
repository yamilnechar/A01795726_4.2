"""
Este programa cuenta la frecuencia de palabras en un archivo de texto.
"""

import sys
import time

def leer_texto(archivo):
  palabras = []
  try:
    with open(archivo, 'r') as f:
      for linea in f:
        palabras.extend(linea.strip().lower().split())
  except:
    print("Error al abrir el archivo:", archivo)
    sys.exit(1)
  return palabras

def contar_palabras(lista):
  conteo = {}
  for palabra in lista:
    if palabra in conteo:
      conteo[palabra] += 1
    else:
      conteo[palabra] = 1
  return conteo

if __name__=="__main__":
  if len(sys.argv)!=2:
    print("Uso: python word_count.py archivo_texto.txt")
    sys.exit(1)

  archivo = sys.argv[1]
  inicio = time.time()

  palabras = leer_texto(archivo)

  if len(palabras)==0:
    print("Error: No hay palabras en el archivo")
    sys.exit(1)

  conteo = contar_palabras(palabras)
  resultado_ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

  tiempo_total = time.time() - inicio

  for palabra, cantidad in resultado_ordenado:
    print(f"{palabra}: {cantidad}")

  print(f"\nTiempo de ejecución: {tiempo_total:.5f} segundos")

  with open("WordCountResults.txt", "w") as f:
    for palabra, cantidad in resultado_ordenado:
      f.write(f"{palabra}: {cantidad}\n")
    f.write(f"\nTiempo de ejecución: {tiempo_total:.5f} segundos")
