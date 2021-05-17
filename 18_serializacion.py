#SERIALIZACION

#Guardar un objeto en un ficherode codigo binario.
# Se utiliza labiblioteca pickle
##################################################

#metodo dump(): guardar datos en fichero binario.
#metodo load(): cargar datos en fichero.


########################################
import pickle

lista_nombre = ["Juan", "Carlos", "Jose"]

#Crear fichero binario
ficherobinario= open("lista nombres","wb")

#Guardar datos en fichero binario
pickle.dump(lista_nombre, ficherobinario)

#Cerrar ficherobinario

ficherobinario.close()


####################################
#LEER ARCHIVO BINARIO
fichero = open("lista nombres","rb")

lista2 = pickle.load(fichero)

print(lista2)