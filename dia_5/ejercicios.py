#ejercicio 1
integers=[3,4,6]
def devolver_distintos(integers):
    suma=0
    for n in integers:
        suma+=n
    if suma>15:
        return max(integers)
    elif suma<10:
        return min(integers)
    elif suma in range(10,15):
        integers.sort()
        return integers[1]

print(devolver_distintos(integers))

#ejercicio2

palabra="carlos"
def orden(palabra):
    mi_set= set() #set no te deja tener palabras repetidas
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set) #convertimos un set a una lista para ordenarla
    mi_lista.sort()
    return mi_lista

print(orden(palabra))

#ejercio3

def ceros_vecinos(*args):

    contador = 0

    for n in args:
        if contador+1 == len(args):
            return False
        elif args[contador]==0 and args[contador+1]==0:
            return True
        else:
            contador+=1
    return False

print(ceros_vecinos(5,3,34,5,3,45,54,4,0,3,0,4,4,0))


#ejercicio4
def contar_primos(numero):
    primos=[2]
    iteracion= 3
    if numero <2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion%n==0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion+=2
    print(primos)
    return len(primos)

primos=contar_primos(50)

print(primos)

