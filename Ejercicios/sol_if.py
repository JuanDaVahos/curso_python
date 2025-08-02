###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)'

### EJERCICIO 1 ###

num1, num2 = input("Por Favor Ingrese dos números: \n").split()
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
  print(f"{num1} es mayor que {num2}")
elif num2 > num1:
  print(f"{num2} es mayor que {num1}")
else:
  print("Los numeros son iguales :3")

### Ejercicio 2 ###

num1 = input("Ingrese el numero 1:\n")
num2 = input("Ingrese el numero 2:\n")

num1 =int(num1)
num2 =int(num2)

res = input("Ingrese una operación: (+, -, *, /)\n")

if res == '+':
  print(f"la suma de los numeros es: {num1 + num2}")
elif res == '-':
  print(f"la resta de los numeros es: {num1 - num2}")
elif res == '*':
  print(f"la multiplicación de los numeros es: {num1 * num2}")
elif res == '/':
  print(f"la divicíon de los numeros es: {num1 / num2}")
else:
  print("Operacíon no valida")

### EJERCICO 3 ###

age_user = int(input("Por favor ingrese un año: \n"))

if (age_user % 4 == 0 and age_user % 100 != 0) or (age_user % 400 == 0):
    print('Tu año es bisiesto')
else:
    print('Tu año no es bisiesto')

### EJERCICIO 4 ###

age = int(input("Por favor ingrese una edad: "))

if age >= 120:
  print("💀💀💀💀")
elif age >= 65:
  print("Adulto mayor")
elif  age >= 18:
  print("Adulto")
elif age >= 13:
  print("Adolecente")
elif age >= 3:
  print("Niño")
else:
  print("Bebé")