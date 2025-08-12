###
# EJERCICIOS (while)
###

import os
os.system('cls')

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("Ejercicio 1:\n")

# numero = 10

# while numero > 0:
#   print(numero)
#   numero-=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("Ejercicio 2:\n")

# contador = 1
# suma = 0

# while contador <= 20:
#   print(contador)
#   contador += 1
#   if contador % 2 == 0:
#     suma = suma + contador
# print(f'suma: {suma}') 

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("Ejercicio 3:\n")

# numero = -1

# while numero < 0:
#   try:
#     numero = int(input('Ingrese un numero entero positivo: \n'))
#     contador = numero
#     if numero < 0:
#       print('Ingresa un numero positivo')
#     else:
#       while contador > 1:
#         contador -= 1
#         numero = numero * contador
#   except:
#     print('Ingresa porfavor un numero entero positivo')

# print(f'Factorial: {numero}')
  


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("Ejercicio 4:\n")

# contrasena = ''

# while len(contrasena) < 8:
#   contrasena = input('Ingrese su contraseña:\n')
#   if len(contrasena) < 8:
#     print('La contraseña debe tener al menos 8 caracteres')
# else:
#   print('Contraseña válida 😀')


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("Ejercicio 5:\n")

# numero = int(input('Ingrese un número por favor:\n'))
# cont = 1

# while cont <= 10:
#   print(f'{numero} x {cont} = {numero*cont}')
#   cont += 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("Ejercicio 6:\n")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input('Ingrese un número entero positivo:\n'))
#     if numero < 0:
#       print('Porfavor Ingrese un número positivo')
#   except:
#     print('Debes Ingresar un número')

#   print('')
#   cont = 2
#   while cont < numero:
#     es_primo = True
#     cont_div = 2

#     while cont_div < cont:
#       if cont % cont_div == 0:
#         es_primo = False
#         print(f'El numero: {cont} no es primo')
#         break
#       cont_div += 1
#     if es_primo:
#       print(f'El numero: {cont} es primo')
#     cont += 1

