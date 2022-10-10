# #77

# """
# mi_archivo = open('prueba.txt')
# primer_linea = mi_archivo.readline()
# print(primer_linea)
# mi_archivo.close()

# """

# #78
# """
# archivo = open('prueba.txt','a')

# archivo.write('\n soy el nuevo texto \n')

# archivo.writelines('hola' + '\n')

# archivo.writelines('como estas')


# archivo.close()

# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# archivo=open('registro.txt','a')

# for i in registro_ultima_sesion:
#     archivo.writelines(i + '\t')

# archivo.close()

# archivo = open('registro.txt','r')

# print(archivo.read())

# archivo.close()"""

#79

import os

 #ruta = os.getcwd() #obtener la ruta en la que estamos


#os.chdir('/Users/gerardoheredia/Desktop/pruebas') #cambiar de ruta de trabajo
#archivo = open('otro_archivo.txt')
#print(archivo.read())

#para saber el nombre del archivo trabajando
#ruta = 'Users/gerardoheredia/Desktop/Python/python dia a dia/prueba.txt'

#elemento= os.path.basename(ruta) #nombre base del elemento

#elemento= os.path.dirname(ruta) #nombre directorio del elemento

#elemento= os.path.split(ruta) #ambos elementos en tuppla

#os.rmdir(ruta) #eliminar ultima carpeta o archivo

#print (elemento)


#from pathlib import Path #Path es un objeto de esta forma

#así de cual sistema operativo puede ser leido
#carpeta = Path('/Users/gerardoheredia/Desktop/Python/python_dia_a_dia/dia_6/prueba.txt')
#archivo = carpeta / 'prueba.txt'
#mi_archivo = open(archivo)
#print(mi_archivo.read())

#print(carpeta.read_text()) #leer el texto del archivo sin necesidad de cambiar a open o read


#if not carpeta.exists():
 #   print("este archivo no existe")
#else:
 #   print("genial existe")


#from pathlib import Path
#path acomodara dependendiendo del software que se trabaja
#base = Path.home()
#guia= Path(base,"Europa","España",Path("Barcelona","Sagrada_familia.txt"))
#copiar una nueva ruta pero con otro archivo
#guia2=guia.with_name("la_pradera.txt")

#guia=Path(Path.home(),"Europa")

#así nos traera todos los documentos txt que encuentre en carpetas y subcarpetas
#for txt in Path(guia).glob("**/*.txt"):
#    print(txt)


#guia= Path("Europa","España","Barcelona","Sagrada_familia.txt")

#en_europa = guia.relative_to(Path("Europa"))

#en_espana= guia.relative_to(Path("Europa","España"))

#print(en_espana)
#print(en_espana)

#print(guia)
#print(guia2)


#from os import system

#system('clear')#para limpiar la consola en mac

