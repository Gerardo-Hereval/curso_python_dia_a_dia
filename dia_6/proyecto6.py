######################### Librerias ###############################
from pathlib import *

import os

from os import system

######################### variables ###############################
#ruta de recetas
ruta=Path(os.getcwd(),"Recetas")
#estado del programa
fin_programa=False



nombre="Carlos"

######################### funciones ###############################
def contar_recetas():
    contar=0
    recetas=[]
    for txt in Path(ruta).glob("**/*.txt"):
        recetas.append(txt)
        contar+=1
    return contar,recetas

def mostrar_categorias():
    contador=1
    categorias=[]
    for x in ruta.iterdir():
        if x.is_dir():
            print(f"[{contador}]  {x.parts[-1]}")
            categorias.append(x)
            contador+=1
    return categorias

def mostrar_recetas(categoria):
    contador=1
    recetas=[]
    for x in categoria.iterdir():
        if x.suffix:
            print(f"[{contador}]  {x.name}")
            recetas.append(x)
            contador+=1
    return recetas
    pass


def leer_receta():
    print("\nTenemos las siguientes categorias: ")
    categorias=mostrar_categorias()

    leer_categoria=int(input("\nEscoge el numero de la categoria que quieres leer: "))
    receta=mostrar_recetas(categorias[leer_categoria-1])
    leyendo_receta=int(input("\nEscoge una receta para leer: "))
    receta=receta[leyendo_receta-1]
    receta=open(receta)
    print(receta.read())
    receta.close()


def crear_receta():
    print("Tenemos las siguientes categorias: ")
    categorias=mostrar_categorias()
    leer_categoria=int(input("\nEscoge el numero de la categoria en la que crearemos la receta: "))
    nombre_receta_nueva=input("\nComo se llamara la nueva receta: ")
    texto_receta_nueva=input("\n Que dira la nueva receta: ")
    ruta_receta_nueva=Path(categorias[leer_categoria-1],f"{nombre_receta_nueva}.txt")
    ruta_receta_nueva.touch()
    archivo=open(ruta_receta_nueva,'a')
    archivo.write(texto_receta_nueva)
    archivo.close()
    print(f'Archivo: {nombre_receta_nueva} creado con exito!')


def crear_categoria():
    print("Tenemos las siguientes categorias: ")
    categorias = mostrar_categorias()
    nombre_categoria_nueva=input("\nComo se llamara la nueva categoria: ")
    ruta_categoria_nueva=Path(ruta,nombre_categoria_nueva)
    ruta_categoria_nueva.mkdir()
    print(f'Archivo: {nombre_categoria_nueva} creado con exito!')


def eliminar_receta():
    print("Tenemos las siguientes recetas")
    contar=1
    for i in recetas:
        print (f"[{contar}] {i.name}")
        contar+=1
    seleccion=int(input("Escoge el numero que desea eliminar: "))
    ruta_eliminar=recetas[seleccion-1]
    os.remove(ruta_eliminar)
    print(f'Archivo eliminado con exito!')

def eliminar_categoria():
    print("Tenemos las siguientes categorias: ")
    categorias = mostrar_categorias()
    seleccion = int(input("Escoge el numero que desea eliminar: "))
    ruta_eliminar = categorias[seleccion - 1]
    os.rmdir(ruta_eliminar)
    print(f'Categoria eliminado con exito!')




######################### pantalla ###############################

while fin_programa==False:
    system('clear')
    print('-'*50)
    print('-' * 50)
    print('-'*5 +" Bienvenido al administrdor de recetas "+'-'*6)
    print('-' * 50)
    print('-' * 50)

    print("Las recetas se encuentran en: ")

    print(ruta)

    contar, recetas = contar_recetas()

    print(f"\nTotal de recetas: {contar}")

    print("\nEscoge una de las siguientes opciones:")
    print("[1] Leer receta")
    print("[2] Crear receta")
    print("[3] Crear categoria")
    print("[4] Eliminar receta")
    print("[5] Eliminar categoria")
    print("[6] Finalizar programa")

    decision=input("\nQue opcion escoges: ")

    if decision == "1":
        leer_receta()
    elif decision == "2":
        crear_receta()
    elif decision == "3":
        crear_categoria()
    elif decision == "4":
        eliminar_receta()
    elif decision == "5":
        eliminar_categoria()
    else:
        fin_programa=True


