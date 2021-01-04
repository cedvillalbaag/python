#Funciones

#Definir una función
def hello ():
    print("Hello World")

#Llamada de la función
hello()



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



#Función con varios parámetros

def add(number_one, number_two):
    return number_one + number_two
#Para visualizar el resultado se imprime
print(add(10,30))



#Definir funciones lambda (funciones anónimas)

t = lambda number_one, number_two: number_one + number_two 
#Para visualizar el resultado se imprime
print(t(12,2))
