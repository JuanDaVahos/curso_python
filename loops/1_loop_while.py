
import os
os.system('cls')


### Sintaxis basica del bucle while ###

# contador = 1

# while contador <= 5:
#   print(contador)
#   contador += 1

# Palabra clave break

# while contador <= 100:
#   print(contador)
#   contador += 1
#   if contador > 5:
#     break

# palabra clave continue
contador = 0

while contador < 10:
  contador += 1
  if contador % 2 == 0:
    continue
  print(contador) 