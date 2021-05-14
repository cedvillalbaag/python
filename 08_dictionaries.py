#DICTIONARIES
#Estructura de datos que permiten almacenar valores de diferente tipo. Define datos a partir de claves y valores. Los elementos almacenados no estan ordenados.

#Definir diccionarios
product = {"name":"book","quantity":3,"price":4.99}
person = {"first_name":"Carlos", "last_name":"Villalba"}

#Ver tipo de dato
print(type(product))

#Ver Metodos y Propiedades
print(dir(product))

#Obtener solo las claves del diccionario
print(person.keys())

#Obtener items de diccionario
print(person.items())

#Limpiar elementos internos del diccionario
person.clear()

#Eliminar diccionario de la aplicación
del person



