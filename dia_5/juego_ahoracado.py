from random import choice, randint
#lista de palabras a elegir
mis_palabras = ['monitor', 'anestesia','hemodinamia','cardio','herramientas','biomedica']

#variable para detener proceso
respuesta=False

#variable para el control de las letras ingresadas
letra=[]

#vidas

vidas=1

#variable repetias
repetidas=[]

#funcion de elegir palabra
def selecPalabra(mis_palabras):
    letras=[]
    palabra=str(choice(mis_palabras))
    for n in range(0,len(palabra)):
        letras.append(palabra[n])
    return palabra,letras

#funcion para elegir dos pistas
def selectPista(palabra,letras):
    adivinadas = []
    pista1=randint(0,len(palabra)-1)
    pista2=randint(0,len(palabra)-1)
    if pista1==pista2:
        pista2 = randint(0, len(palabra)-1)
    else:
        pass
    for n in range(0,len(palabra)):
        adivinadas.append('_')
    adivinadas[pista1]=letras[pista1]
    adivinadas[pista2]=letras[pista2]
    return adivinadas

#quitar vidas
def quitarVida(vidas):
    vidas-=1
    return vidas

#agregar letras adivinadas

def encontrarLetras(letra,letras):
    contador=0
    letrasAdivinadas=[]
    for n in letras:
        if letra==n:
            letrasAdivinadas.append(contador)
            contador+=1
        else:
            contador+=1
    return letrasAdivinadas

#remplazar letras adivinadas

def remplazarLetras(adivinadas,letrasAdivinadas):
    for n in letrasAdivinadas:
        adivinadas[n]=letras[n]
    return adivinadas


#funcion para validar letra
def validarLetras(letraNueva,repetidas):
    if letraNueva in repetidas:
        return False, "repetida"
    elif letraNueva==' ' or letraNueva=='':
        return False, "espacio"
    else:
        return True,"ok"
    return False



#funciones iniciales
palabra,letras=selecPalabra(mis_palabras)
adivinadas=selectPista(palabra,letras)

print(palabra)

nombre = input("Dime tu numbre: ")
print(f"¡Hola {nombre}!, este es el juego del ahorcado, \nla palabra ya fue elegida, trata de adivinarla\n ¡Suerte!")

print("\n", adivinadas)

while respuesta==False:

    if letra!=[]:
        repetidas.append(letra[-1])

    letra.append(input("\ningrese una letra: ").lower())
    estado,razon=validarLetras(letra[-1],repetidas)

    if estado==True:

        letrasAdivinadas = encontrarLetras(letra[-1], letras)
        adivinadas = remplazarLetras(adivinadas, letrasAdivinadas)

        if letras == adivinadas:
            print(f"Felicidadesssssss {nombre}, eres un campeon, has ganado, la palabra era: {palabra}")
            respuesta = True

        elif letra[-1] in letras:
            print(f"¡Adivinaste una letra! Felicidades!!! continua así, tienes : {vidas} vidas")
            print("\n", adivinadas)

        else:
            vidas=quitarVida(vidas)

            if vidas>0:
                print(f"Lo siento {nombre}, te equivocaste, tienes {vidas} vidas")

            elif vidas==0:
                print(f"Lo siento {nombre}, has perdidooooooo!!!")
                respuesta = True
                print(respuesta)

            print("\n", adivinadas)
    elif estado==False:
        if razon=="repetida":
            print(f"{nombre}, Repetiste la letraaaaaa, intenta con otraaaaa!!!")
        elif razon=="espacio":
            print(f"{nombre}, estas ingresando algo que no debes,intenta de nuevo!!!")

