### Más Metodos utiles ###

#ordenar una lista
numeros = [1, 43, 23, 45, 12, 76, 21, 53]

# sort, organiza la lista de menor a mayor pero no hace ningun return 
numeros.sort() # esto modifica esta misma lista

# para guardar o hacer una copia de la lista (sorted)
organizado = sorted(numeros)
print(organizado) #parece igual pero ahora tenemos la lista ordenada y desordenada tambien

# ordenar cadenas de texto
cadenas = ["pera", "manzana", "plátano", "kiwi"]
cadenas_sorted = cadenas.sort() # ordena la lista de cadenas en orden alfabético

# soretd es sensible a mayusculas y minusculas
cadenas = ["pera","Pera", "manzana", "plátano","Platano", "kiwi"]
cadenas.sort()
print(cadenas) # ['Pera', 'Platano', 'kiwi', 'manzana', 'pera', 'plátano']

# para ordenarlas en orden alfabético ignorando mayusculas y minusculas
cadenas.sort(key=str.lower)
print(cadenas) # ['kiwi', 'manzana', 'pera', 'Pera', 'Platano', 'plátano']

### Cosas utiles para las listas, no son metodos ###

# Para contar cuantas veces aparece un elemento en una lista usamos el motodo count (contar)
animals = ['🐶', '😺', '🐼' ,'🐼']
print(animals.count('🐼')) # el emoji de 🐼 aparece 2 veces por lo que la consola mostrara (2)

# tambien podemos comprobar si en una lista existe cierto elemento
print('🐶' in animals) # esto duvuelve un booleano, en este caso es True, ya que si existe el elemento en la lista

