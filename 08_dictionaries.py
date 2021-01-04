#dictionaries 
#define datos a partir de claves y valores

#Definir diccionario
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

#Limpiar elementos internos
person.clear()

#Eliminar diccionario
del person



