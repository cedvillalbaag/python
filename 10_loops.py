#Loops : Bucles o iteradores

foods = ["apples", "bread", "cheese", "milk"]

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


#Bucle Numero
for number in range(1,8):
    print(number)


#Bucle Cadena de Texto
for letter in "Hello World":
    print (letter)



#Bucle While (Similar a If)
count = 4

while count <= 10:
    print(count)
    count = count + 1


