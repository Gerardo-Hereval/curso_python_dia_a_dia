def suma():
    n1 = int (input("numero 1: "))
    n2=int (input("numero 2: "))

    print(n1+n2)
    print("gracias por sumar")




'''# error de input
try:
    #codigo a probar
    suma()
except:
    # codigo a ejecutar si hay un error
    print("algo no ha salido bien")
else: 
    #codigo a ejecutar si no hay un error
    print("hisiste todo bien")
finally:
    #codigo que se va a ejecutar de todos modos
    print("eso es todo")'''

'''#para contestar dependiendo del error
try:
    #codigo a probar
    suma()
except TypeError:
    # codigo a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    # codigo a ejecutar si hay un error
    print("Ese no es un numero")
else: 
    #codigo a ejecutar si no hay un error
    print("")
finally:
    #codigo que se va a ejecutar de todos modos
    print("eso es todo")'''

def pedir_numero():
    while True:
        try:
            numero= int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()