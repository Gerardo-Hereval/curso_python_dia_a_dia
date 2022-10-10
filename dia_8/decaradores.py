
# from xml.dom import minicompat


# def cambiar_letras(tipo):
    
    
#     def mayusculas(texto):
#         print(texto.upper())


#     def minusculas(texto):
#         print(texto.lower())
    
#     if tipo=="may":
#         return mayusculas
#     elif tipo == "min":
#         return minusculas


# operacion = cambiar_letras('may')

# operacion ('palabra')


def decorar_saludo (funcion):


    def otra_funcion(palabra):
        print ('Hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

#es una posible forma con los @
#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


#@decorar_saludo
def minusculas(texto):
    print(texto.lowe())


mayusculas_decoradas = decorar_saludo(mayusculas)

mayusculas_decoradas('Car')
