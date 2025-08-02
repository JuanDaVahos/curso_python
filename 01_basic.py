# print ("Hello world")
# print ("Python","is","beautiful", sep = "")
# print ("Python"," is ","beautiful", end = ".")


# # casting type
# # cambiar de un tipo a otro

# print ("Converción de tipos: ")
# print ("3")
# print (type(int("3")))

# print (int(3.1416))
# # no redondea los decimales
# print (int(3.9416))

# # para redondear se utiliza raund, y cuando es .5 exacto redondea al numero par más cercano 

# print (round(3.5)) #4
# print (round(2.5)) #2


# ### Variables ###

# #name = Valor

name = "Sergio"
# print (name)

# no hace falta declarar el tipo de variable
# python es de tipado dinámico

# Tipado fuerte, no realiza conversiones de tipo automatico
# f-strings

print (f"Mi nombre es {name}")

# Forma no recomendada de asignar variables

name, age, city = "Sergio", 25, "Bogota"

# converciones de nombres de variables
# snake_case

mi_nombre_de_variable = "Es Correcto el snake_case"

## python no tiene constantes, su pueden emular pero no las trae por defecto ##

# para simular constantes se utiliza mayusculas (Uptercase)

PI = 3.1416
