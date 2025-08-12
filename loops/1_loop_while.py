
import os
os.system('cls')

# ### Sintaxis basica del bucle while ###

# contador = 1

# while contador <= 5:
#   print(contador)
#   contador += 1

# ## Palabra clave break

# while contador <= 100:
#   print(contador)
#   contador += 1
#   if contador > 5:
#     break

# ## palabra clave continue

# while contador < 10:
#   contador += 1
#   if contador % 2 == 0:
#     continue
#   print(contador)

# ## while en python tambien usa else

# # el else en un while, en python se ejecuta cuando el while a finalizado, es decir, cuando se deja de cumplir la condición

# while contador <= 10:
#   print(contador)
#   contador += 1
# else:
#   print('El while a finalizado')

# ## Para que usar else en un while?

# # el else puede ser util cuando te quieres asegurar de que si o si se deja de cumplir la condicion
# # cuando se usa la palabra clave BREAK no se ejecuta el else

# while contador <= 10:
#   print(contador)
#   contador+=1
#   if contador == 5:
#     break
# else:
#   print('esto no se mostrara')

# ## Ejercicio practico con while

# # pedirle al usuario un número que tiene
# # que ser positivo si no, no le dejamos en paz

# numero = -1

# while numero < 0:
#   numero = int(input('Ingrese un número positivo:\n'))
# else:
#   print('Muchas gracias')

# ## Manejar errores con try & execpt

numero = -1

while numero < 0:
  try:
    numero = int(input('Ingrese un número positivo:\n'))
    if numero < 0:
      print('😠😠 POSITIVO!! 😠😠')
  except:
    print('debes ingresar un numero positivo')
else:
  print(f'Introduciste el número {numero}')
