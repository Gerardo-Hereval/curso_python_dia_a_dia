#cuidar el espacio de memoria del equipo, genera poco a poco el resultado
#cambiando return a yield


def mi_funcion():
    return 4

def mi_generador():
    yield 4

print(mi_funcion())

print(mi_generador())# no lo va a imprimir  hasta hacer lo siguiente

g=mi_generador()

print(next(g))