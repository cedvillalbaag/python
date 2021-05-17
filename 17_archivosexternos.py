#ARCHIVOS EXTERNOS

#FASES
#creacion - apertura - manipulacion - cierre



######################################################

#IMPORTAR MODULO IO
from io import open

######################################################

#ABRIR/ CREAR ARCHIVO EXTERNO
#Modo lectura: "r"
# Modo escritura "w"

#Si elarchivo no esta creado, el codigo lo crea.

archivo_texto = open("archivo1.txt", "w")



#######################################################

#Incluir contenido de una variable en un archivo de texto

var1 = "este es una prueba de texto \n realizado en mayo2021"

archivo_texto.write(var1)

archivo_texto.close()


########################################################

#Leer y extraer contenido de un archivo de texto

archivo_texto2 = open("archivo2.txt", "r")

texto = archivo_texto2.read()

archivo_texto2.close()

print(texto)

#######################################################
#ABRIR ARCHIVO - METODO READLINES

#permite almacenar linea a linea el texto en una lista.

archivo_texto2 = open("archivo2.txt", "r")

lineas_texto = archivo_texto2.readlines()

archivo_texto2.close()

#Imprimir una linea de texto en especifico
print(lineas_texto[2])

################################################

#AGREGAR TEXTO A ARCHIVO- METODO APPEND

archivo_texto = open("archivo1.txt", "a")

var1 = "\n Agregar nuevo texto:\n este es una prueba de texto agregado \n realizado en julio2021"

archivo_texto.write(var1)

archivo_texto.close()