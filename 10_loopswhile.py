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