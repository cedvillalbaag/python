#LISTAS - EQUIVALENTE A LOS ARRAYS - VECTORES

#Estructuras de datos que permiten almacenar varios valores, de diferentes tipos, se pueden expandir
#Siempre se comienza a numerar desde la posicion 0.


#Diferentes tipos de datos
demo_list = [1, "hola", 10.2, [10, 2]]
#Un mismo tipo de dato
colors = ["black", "red", "yellow"]


#Crear una lista utilizando el constructor
numbers_list = list((1, 2, 3, 4))
#Imprimir una lista
print(numbers_list)



#Crear una lista basada en rango
r = list(range(1, 10))
print(r)

################################################################

#METODOS PARA LISTAS

#Imprimir los metodos que puedo utilizar en las listas
print(dir(colors))

#Conocer la longitud de la lista - cantidad de elementos
print(len(colors))

#Acceder a un elemento de la lista en específico
print(colors[1])

#Acceder a un elemento espefífico de orden inverso de la lista
print(colors[-2])

#Acceder a una parte de la lista
print(colors[0:1])

#Acceder a elementos desde la posicion dada hasta el final de la lista:
nombres = ["Carlos","Jorge", "Alonso", "Pedro", "Juan"]
print(nombres[2:])


#Saber si un elemento existe dentro de lista
print("green" in colors)

#Saber en que posición se encuentra un elemento en la lista
print(nombres.index("Carlos"))

#Cambiar un elemento de la lista
colors[2] = "orange"
print(colors)

#Append - agregar un SOLO elemento al final de la lista
colors.append("blue")
print(colors)

#Extend - agregar varios elementos a la lista
colors.extend(["brown","white"])
print(colors)

#Insert - Agregar un elemento dentro de una posicion en la lista
colors.insert(1,"purple")
print(colors)

#Pop - Remover ultimo elemento de lista - con numero elimina el del indice
colors.pop()
print(colors)

#Remove - Remover elemento especifico de la lista
colors.remove("blue")
print(colors)

#Clear - Remover todos los elementos de la lista
colors.clear()

#Sort - Ordenar elementos de forma alfabética o por valores
colors = ["black", "red", "yellow"]
colors.sort()
print(colors)

#Sort - Ordenar elementos de forma inversa
colors.sort(reverse=True)

#Index - Obtener el indice
print(colors.index("red"))

# Count - Contar elemento dentro de la lista
print(colors.count("black"))
print(colors)


#Unir dos listas existentes
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]

lista3 = lista1 + lista2
print(lista3)


# Repetir una lista N veces
lista4 = [2,4,6]
lista5 = 2*lista4

print(lista5)








