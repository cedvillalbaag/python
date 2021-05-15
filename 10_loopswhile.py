#Importar librerías
import math

##########################################################################
#BUCLE WHILE (SIMILAR A IF) - "CUANDO"

#Bucle indeterminado: no sabemos cuantas veces se irá a ejecutar

#Sintaxis
count = 4

while count < 10:
    print(count)
    count = count + 1


###########################################################################
#Otro ejemplo - Concatenando con texto
#Importante validar las condiciones y el incremento para que finalice el bucle

var1 = 5

while var1 < 20:
    print ("Ejecución de código: " + str(var1))
    var1 = var1 + 1
print("Termino la ejecución")



###############################################################################
#OTRO EJEMPLO

edad = int(input("Ingrese su edad: "))

###############################################################################
#SALIR DEL BUCLE CON EL USO DE BREAK

print("calculo de raiz cuadrada")


numero = int(input("Agregue un numero:  "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raiz de numero negativo")

    if intentos == 2:
        print("Haz consumido demasiados intentos")
        break;
    numero = int(input("Agregue numero por favor:  "))
    if numero < 0:
        intentos = intentos + 1
if intentos < 2:
    solucion = math.sqrt(numero)
    print (int(solucion))