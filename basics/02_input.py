## los inputs son para recibir informacion del usuario
## input("pregunta") # pregunta al usuario

name = input("What is your name? ")
print ("Hello", name)

# un input siempre devuelve un string

## puedes tomar varios valores de un solo imput

# split por defecto separa los valores por espacios, pero puedes cambiarlo si así lo deseas :3

name, age = input("What is your name and age? ").split()
print ("Hello", name, "you are", age)

