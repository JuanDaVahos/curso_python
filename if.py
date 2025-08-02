## usaremos el if en python, ya lo se pero es bueno repasarlo

# python no usa llaves
# python sabe el bloque de codigo por tabulaciones

#importar modulo 

import os
os.system("cls")

edad = 18

if edad >= 18:
  print ("Eres mayor de edad")
else :
  print ("Eres menor de edad")

# para hacer 3 o más condiciones se usa elif

print ("Sintaxis elif con ejemplo de notas")

nota = 7

# una ves se cumple una condicion se ignoran las demas, =)
# por eso no se muestran dos mensajes o más al mismo timpo

if nota >= 9:
  print ("Excelente")
elif nota >= 7:
  print ("Muy bien")
elif nota >= 5:
  print ("Bien")
else:
  print ("Insuficiente")

## La ternaria

# [código si cumple la condición] if [condición] else [código si no cumple la condición]

print ("Sintaxis ternaria con ejemplo de notas")

edad = 17

print ("Es Mayor de edad" if edad >= 18 else "Es Menor de edad")