#GENERADORES

#Estructuras que extraen valores de una función y se almacenan en objetos iterables (que se pueden recorrer por un bucle).


#Se almacenan de uno en uno. Se consigue el estado de suspensión hasta que vuelva a ser llamada la función. El control de flujo de ejecución pasa nuevamente al algoritmo.

#Ventaja en eficiencia frente a las funciones porque no genera la lista completa de valores.


#################################################################


def generapares(limite):
    num = 1

    while num<limite:
        yield num*2
        num = num + 1

devuelvepares = generapares(10)
#imprimiendo la lista entera
for i in devuelvepares:
    print(i)

#######################################################

def generapares(limite):
    num = 1

    while num<limite:
        yield num*2
        num = num + 1

devuelvepares = generapares(10)
#imprimiendo la lista entera

print(next(devuelvepares))

print("podria ir más codigo")

print(next(devuelvepares))
