#CONDICIONALES

#Evaluar si la condición se cumple o no.


#Operadores de Comparación (==, !=, <, >, >=, <=)

3 > 2


########################################################################

#Conditional If
y=50
if y==50:
    resultado = 50
print("y = 50 unds")

########################################################################
#OTRO EJEMPLO DE FUNCION CON IF


print("programa de evaluación de notas")

valor = input("Introduce la nota de un alumno:    ")
# en python el input es tomado como texto

def calculo(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "reprobado"
    return valoracion


print(calculo(int(valor)))


########################################################################

#Condicional If-Else (SI - SI NO ES VERDAD)
x=40

if x<30:
    print ("x is less than 30")
else:
    print ("x is more than 30")




########################################################################
#Conditional Elif
color = "red"

if color == "red":
    print("the color is red")
elif color == "green":
    print ("the color is green")
else:
    print("any color")  



#If Anidado
name = "Carlos"
last_name = "Villalba"

if name == "Carlos":
    if last_name =="Villalba":
        print("Tu eres Carlos Villalba")
    else:
        print("Tu no eres Carlos Villalba")
else:
    print ("Tu no eres Carlos")


#Operadores Lógicos ---- AND, OR, NOT
m = 30

if m<50 and m>20:
    print("m es menor que 50 y mayor que 20")
else:
    print("fuera de rango")























