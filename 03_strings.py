#STRINGS (CADENAS DE TEXTO)

mystr = "Hello World1"
mystr2 = "hello,world"


######################################################################################

#PROPIEDADES Y METODOS

#Ver Propiedades y Metodos para Strings
print(dir(mystr))

#################

#Metodos: nos permiten alterar los datos de la cadena

#Convertir cadena de texto a formato Título
print(mystr2.title())

#Convertir cadena de texto a formato Mayuscula
print(mystr.upper())

#Convertir cadena de texto a formato minuscula
print(mystr.lower())

#Convertir cadena de texto en primera en minuscula y resto en mayuscula
print(mystr.swapcase())

#Convertir cadena de texto por Primeraletra en mayuscula
print(mystr.capitalize())
   
#Reemplazar cadena de texto
print(mystr.replace("Hello","bye"))

#Metodos Encadenados - Encadenación de métodos
print(mystr.replace("Hello", "bye").upper())


#Contar: Cuenta un caracter dentro de una cadena de texto
print(mystr.count("l"))

#Verifica si cadena de texto comienza con 
print(mystr.startswith("Hello"))

#Verifica si cadena de texto termina con
print(mystr.endswith("ld"))

#Dividir cadena de texto por espacios (Crea una lista)
print(mystr.split())

#Dividir cadena de texto por caracter (Crea una lista)
print(mystr2.split(","))

#Encontrar la Posicion de un caracter en la cadena de texto
print(mystr.find("o"))

#Cantidad de caracteres en una cadena de texto
print(len(mystr))

#Indice de un caracter
print(mystr.index("e"))

#Saber si es numerico
print(mystr.isnumeric())

#Saber si es alfanumerico
print(mystr.isalpha())

#Imprimir un caracter teniendo en cuenta la posición en la cadena de texto
print(mystr[0])

#Imprimir un caracter teniendo la posición inviertiendo la cadena de texto
print(mystr[-1])
print(mystr[-2])

#Concatenar cadenas de texto
print("Mi nombre es Carlos " + mystr)
print(f"Mi nombre es Carlos {mystr}")
