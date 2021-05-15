#FUNCIONES
#Conjunto de código que realiza una tarea específica.

#Pueden devolver valores o no.
#Pueden tener argumentos o no.
#denominadas metodos cuando se encuentran definidas dentro de una clase.
#Reutilizar código
# Cuando se coloca * iniciando el argumento de una función indica que no se sabe cuantos elementos formaran parte del argumento y sera una tupla
########################################################

#Definir una función
def hello ():
    print("Hello World")

#Llamada de la función
hello()



#####################################################
#Función con parámetro
def hello (name):
    print("Hello " + name)

#Llamada de la función
hello("Carlos")



#Función con parámetro por defecto
def hello (name="Person"):
    print("Hello " + name)

#Llamada de la función
hello()


#####################################################
#Función con varios parámetros

def add(number_one, number_two):
    return number_one + number_two
#Para visualizar el resultado se imprime
print(add(10,30))


def sum(num1, num2):
    resultado = num1+num2
    return resultado

almacena_resultado = sum(1,2)
print(almacena_resultado)



############################################################################
#Definir funciones lambda (funciones anónimas)

t = lambda number_one, number_two: number_one + number_two 
#Para visualizar el resultado se imprime
print(t(12,2))
