#TUPLAS

#Conjunto de datos que no van a cambiar y que no se pueden modificar
# La tupla es más rápida al momento de ejecutarse


#Definir tuplas
x = (1, 2, 3, 4, 5)
months = ("Enero", "February")
y = tuple((1, 2, 2))

#Utilizar el constructor de una tupla para definirla
lista1 = [2,4,6,8]
tupla1 = tuple(lista1)
print(tupla1)


#Ejemplo de tupla
locations = {
    (35.123,56.235):"Tokyo",
    (65.32,48.85):"Miami",
    (57.36,54.25):"Caracas"
}

#Imprimir tuplas
print(x)
print(y)

#Buscar un elemento dentro de una tupla
print("Enero" in months)


#Métodos y Propiedades que pueden ser utilizados en una tupla
print(dir(x))

#Imprimir solo un elemento de la tupla
print(x[0])

#Eliminar tupla
del x

#Conocer cuantas veces se encuentra un elemento dentro de una tupla
print(tupla1.count(2))

#Cantidad de elementos de una tupla
print(len(tupla1))

#Crear tuplas unitarias
tupla_unit = ("Carlos",)
print(tupla_unit)

#Desempaquetado de tupla: asignar los valores de una tupla a variables
tupla2 = ("Carlos", "Villalba", 2210, "M")
nombre, apellido, documento, sexo = tupla2
print(nombre)
