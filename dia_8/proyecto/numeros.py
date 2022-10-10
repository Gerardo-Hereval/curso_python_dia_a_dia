"""Turnero de farmacia

perfumeria, farmacia y cosmeteria


a cual de los tres debe dirigirse

dependiendo del lugar es el tipo de turno

p-perfumeria f-farmacia y c-cosmeteria """




#generador para perfumeria
def turno_perfumeria():
    for i in range(1,1000):
        yield f"P - {i}"

#generador para farmacia
def turno_farmacia():
    for i in range(1,1000):
        yield f"F - {i}"

#generador para cosmeteria
def turno_cosmeteria():
    for i in range(1,1000):
        yield f"C - {i}"

p=turno_perfumeria()
f=turno_farmacia()
c=turno_cosmeteria()

#funcion para decorar turno
def decorar_turno(ubicacion):
    print("\n" + "*" * 23)
    print('\nHola, este es tu turno:')
    if ubicacion=='P':
        print(next(p))
    elif ubicacion=='F':
        print(next(f))
    else:
        print(next(c))
    print('Espere a su turno por favor')
    print("\n" + "*" * 23)


"""#pruebas de funciones

decorar_turno('P')
decorar_turno('F')
decorar_turno('C')
decorar_turno('P')
decorar_turno('F')
decorar_turno('C')
decorar_turno('P')
decorar_turno('F')
decorar_turno('C')"""