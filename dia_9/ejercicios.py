"""from collections import Counter, defaultdict, namedtuple

numeros = [1,2,3,5,6,3,2,3,3,5,5,6,7,7,8,8,3]

print(Counter(numeros))#contamos las veces que se repite un numero, tambien se puede con letras
serie = Counter(numeros)#contamos las veces que se repite un numero, tambien se puede con letras

print(serie.most_common())# el más comun, si ponemos un numero en common limita la cantidad

print('*'*25 +'\n')
print('*'*25 +'\n')


mi_dic = defaultdict(lambda:'nada')#para cuando en un diccionario no tiene un valor, cuando lo llames salga nada

mi_dic['uno'] = 'verde'

print(mi_dic['dos'])

print(mi_dic)

print('*'*25 +'\n')
print('*'*25 +'\n')


Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)

print(ariel[2])

print(ariel.nombre)"""


############################################
########## clase de modulos OS #############
############################################
"""

import os
import shutil
import send2trash

archivo = open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

#shutil.move('/Users/gerardoheredia/Desktop/curso.txt',"/Users/gerardoheredia/Documents/Python/python_dia_a_dia/dia_9") #mover documentos

#os.unlink()#elimina una documento en una ruta especifica

#os.rmdir()#elimina una carpeta vacia

#shutil.rmtree()#elimina todo lo que le pongas de manera definitiva

#send2trash.send2trash('curso.txt')# se manda al basurero

print(os.walk('/Users/gerardoheredia/Documents'))#nos mostrata todo lo que tiene adentro, almacena ruta, subcarpeta y archivo

ruta ='/Users/gerardoheredia/Documents'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta:{carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print ('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')



#arch.startswith('2015') # para buscar archivos que empiecen con 2015"""



############################################
########## clase de modulos Datetime########
############################################

#import datetime


#mi_hora = datetime.time(17,35)#horas,minutos

#print(mi_hora.hour)


#mi_dia = datetime.date(2025,10,17)

#print(mi_dia.today())



#from datetime import datetime


#mi_fecha = datetime(2025,5,15,22,10,15,2500)
#print(mi_fecha)


