#LISTAS

#Diferentes tipos de datos
demo_list = [1, "hola", 10.2, [10, 2]]

#Un mismo tipo de dato
colors = ["black", "red", "yellow"]

#Utilizando el constructor
numbers_list = list((1, 2, 3, 4))


#Imprimir una lista
print(numbers_list)


#Crear una lista basada en rango
r = list(range(1, 10))
print(r)


#Métodos que puedo utilizar con las listas
print(dir(colors))


#Conocer la longitud de la lista (Cantidad de elementos)
print(len(colors))

#Imprimir un elemento de la lista
print(colors[1])

#Imprimir un elemento inverso de la lista
print(colors[-2])

#Saber si un elemento existe dentro de lista
print("green" in colors)

#Cambiar un elemento de la lista
colors[2] = "orange"
print(colors)

#Append - agregar un elemento a la lista
colors.append("blue")
print(colors)

#Extend - agregar varios elementos a la lista
colors.extend(["brown","white"])
print(colors)

#Insert - Insertar un elemento dentro de una posicion en la lista
colors.insert(1,"purple")
print(colors)

# Pop - Remover ultimo elemento de lista - con numero elimina el del indice
colors.pop()
print(colors)

# Remove - Remover elemento especifico
colors.remove("blue")
print(colors)

# Clear - Remover todos los elementos
colors.clear()

#Sort - Ordenar Colores
colors = ["black", "red", "yellow"]
colors.sort()
print(colors)

#Sort - Ordenar de forma inversa
colors.sort(reverse=True)

#Index - Obtener el indice
print(colors.index("red"))

# Count - Contar elemento
print(colors.count("black"))
print(colors)








