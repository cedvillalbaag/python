#LOOPS - BUCLES O ITERADORES

#DETERMINADOS: Se repetiran un numero determinado de veces. Se sabe cuantas veces se a a ejecutar.

#INDETERMINADO: Se ejecutan un numero indeterminado de veces. El numero de veces dependerá de las circunstancias durante la ejecución del programa.

#SINTAXIS:
#for variable in elementoarecorrer(LISTA,TUPLA,TEXTO):

for i in ("Mercurio","Venus","Tierra","Marte"):
    print(i)

###################################################################


foods = ["apples", "bread", "cheese", "milk"]

#Recorrer un elemento de la lista
print(foods[0])


#Recorrer cada uno por separado
for food in foods:
    print(food)


#Recorrer cada elemento de la lista
for food in foods:
    if food == "cheese":
        print(food)    


#Recorrer cada elemento de la lista y salir del bucle cuando se cumpla la condición
for food in foods:
    if food == "cheese":
        break
    print(food)    



for food in foods:
    if food == "cheese":
        print("Tienes que comprar esto:")
    print(food)  


#Bucle para rango de números
for number in range(1,8):
    print(number)


#Bucle Cadena de Texto
for letter in "Hello World":
    print (letter)

#Imprimir texto del bucle en una sola línea
print("Ejemplo de imprimir en una sola línea:")
materias = ["matematica","fisica","castellano","ciencias"]

for materia in materias:
    print(materia, end= " ")


print("ejemplo de imprimir texto junto a la variable i")
for i in range(5):
    print(f"Valor de la variable {i}")


#Variando los parametros de Range - (Inicio, fin, incremento)
#Imprimir valor de la variable con incremento
for i in range(2,15,3):
    print(f"Valor de la variable {i}")    


##########################################################################
#Bucle While (Similar a If)
count = 4

while count <= 10:
    print(count)
    count = count + 1


