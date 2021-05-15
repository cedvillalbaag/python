#EXCEPCIONES
#errores que ocurren durante la ejecución del programa y hacen que el programa no se ejecute.
#Las excepciones permiten manejar los errores para que el codigo pueda continuar ejecutandose.
# try - except

###################################################################

#GENERAR UN ERROR EN EL CODIGO PARA APLICAR LA EXCEPCION

var1= int(input("Ingrese el primer numero: "))
var2= int(input("Ingrese el segundo numero: "))
operacion = (input("Ingrese la operación: "))

if operacion == "dividir":
    try:
        print(var1/var2)

    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        

print("operacion ejecutada")


##########################################################################
#CAPTURA DE VARIAS EXCEPCIONES


def divide():

    try:
        op1 = float(input("Introduce el numero:  "))
        op2 = float(input("Introduce el numero2: "))

        print("la división es : "+ str(op1/op2))
    
    except ValueError:
        print("El valor introducido es erroneo")

    except ZeroDivisionError:
        print("No se puede dividir entre 0")

#BUCLE INFINITO

#errores de varios tipos



##########################################################################
#CLAUSULA FINALLY





