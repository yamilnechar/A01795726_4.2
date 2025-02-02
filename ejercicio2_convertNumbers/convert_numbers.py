"""
Este programa convierte números de un archivo de texto a binario y hexadecimal
sin usar las funciones predefinidas bin() y hex().
"""

import sys
import time

def leer_numeros(archivo):
  numeros = []
  try:
    with open(archivo, 'r') as f:
      for linea in f:
        try:
          numeros.append(int(linea.strip()))
        except:
          print("Valor no numérico ignorado:", linea.strip())
  except:
    print("Error al abrir el archivo:", archivo)
    sys.exit(1)
  return numeros

def convertir_a_binario(num):
  binario = ""
  while num > 0:
    binario = str(num % 2) + binario
    num //= 2
  return binario if binario else "0"

def convertir_a_hexadecimal(num):
  hex_chars = "0123456789ABCDEF"
  hexadecimal = ""
  while num > 0:
    hexadecimal = hex_chars[num % 16] + hexadecimal
    num //= 16
  return hexadecimal if hexadecimal else "0"

if __name__=="__main__":
  if len(sys.argv)!=2:
    print("Uso: python convert_numbers.py archivo_numeros.txt")
    sys.exit(1)

  archivo = sys.argv[1]
  inicio = time.time()

  numeros = leer_numeros(archivo)
  
  if len(numeros)==0:
    print("Error: No hay números válidos en el archivo")
    sys.exit(1)

  resultados = []
  for num in numeros:
    binario = convertir_a_binario(num)
    hexadecimal = convertir_a_hexadecimal(num)
    resultados.append(f"Número: {num} | Binario: {binario} | Hexadecimal: {hexadecimal}")

  tiempo_total = time.time() - inicio

  print("\n".join(resultados))
  print(f"\nTiempo de ejecución: {tiempo_total:.5f} segundos")

  with open("ConversionResults.txt", "w") as f:
    f.write("\n".join(resultados))
    f.write(f"\nTiempo de ejecución: {tiempo_total:.5f} segundos")
