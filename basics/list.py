## listas en python

#como crear una lista

import os
os.system("cls")

lista1 = [1, 2, 3, 4, 5] #lista de numeros enteros
lista2 = ["manzana", "pera", "plátano"] #lista de cadenas
lista3: list[int | str] = [1, "manzana", 4, "peras"] #lista tipada correctamente

lista_vacia = [] #lita vacia
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia) #error justo por que esta vacia
print(lista_de_listas)
print(matrix)

## Acceso a elementos por índice
#puedes usar índices negativos para empezar desde la ultima posición o índice
print(lista1[0])
print(lista1[1])
print(lista1[-1])
print(lista1[-2])

#aceder a lista de listas 
print(lista_de_listas[1][0]) #3

## slicing (rebanado) de listas
print(lista1[1:4]) #[2, 3, 4] el 5 no es visible ya que es el tope el ultimo índice
print(lista1[:3])  #[1, 2, 3] así puede indicar que quieres los primero 3
print(lista1[2:])  #[3, 4, 5] empieza a mostrar desde el índice 2

# Puedes crear una copia de la lista
print(lista1[:])   #[1, 2, 3, 4, 5]

# Tambien puedes saltarte índices
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # [1, 3, 5, 7]
print(lista1[::3]) # [1, 4, 7]
# Tambien puedes empezar una lista desde el final
print(lista1[::-1]) # [8, 7, 6, 5, 4, 3, 2, 1]

# Python no admite que puedas modificar un índice inexistente
# lista1[120] = 9
# print(lista1) #list assignment index out of range

## Añadir elementos a la lista

#forma larga y menos eficiente
lista1 = [1, 2, 3]
lista1 = lista1 + [4, 5, 6]
print(lista1) # [1, 2, 3, 4, 5, 6]

#forma corta y más eficiente

lista1 += [7, 8, 9]
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

### METODOS CON LAS LISTAS ###

lista1 = [1, 2, 3, 4, 5]

#para añadir un elemento al final de la lista
lista1.append(6)

#para insertar un elemento en cualquier índice de la lista
lista1.insert(1, 5)

#para agregar varios elementos al final de la lista
lista1.extend([7, 8, 9])

#para eliminar la primera aparición de la lista
lista1.remove(5) #elimina la primera aparición del 5 en la lista

#para eliminar un elemento de un índice (por defecto elimina el ultimo elemento de la lista, te hace un return del elemento)

ultimo = lista1.pop()
print(ultimo)

lista1.pop(1)
print(lista1)

#para eliminar todos los elementos de la lista
lista1.clear()
print(lista1)

#para eliminar un rango de una lista podemos usar el delete (del)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
del lista1[1:3]
print(lista1)