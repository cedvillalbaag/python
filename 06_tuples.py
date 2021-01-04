#Tuplas - Queremos definir un conjunto de dato que no van a cambiar

#Definir tuplas
x = (1, 2, 3, 4, 5)
months = ("Enero", "February")
y = tuple((1, 2, 2))

locations = {
    (35.123,56.235):"Tokyo",
    (65.32,48.85):"Miami",
    (57.36,54.25):"Caracas"
}


#Imprimir tuplas
print(x)
print(y)


#Métodos y Propiedades que pueden ser utilizados en una tupla
print(dir(x))


#Imprimir solo un elemento de la tupla
print(x[0])


#Eliminar tupla
del x


