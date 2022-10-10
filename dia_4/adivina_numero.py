#hacer un juego que adivine el numero aleatorio y que  de pistas de cual numero es, se debe adivinar con solo
#8 oportunidades

from random import randint
estimado=0
intentos= 0
num_secreto= randint(1,100)

nombre = input("Dime tu numbre: ")

print(f"Bueno {nombre}, he pensado un numero entre 1 y 100 \n Tienes 8 intentos para adivinar")

while intentos<5:
    estimado = int(input("Cuál es el número?: "))
    intentos +=1
    if estimado not in range(1,100):
        print("Tu numero esta fuera del rango mensionado, ya perdiste una oportunidad jiji")
        continue
    if estimado<num_secreto:
        print("Mi numero es más alto")
    elif estimado> num_secreto:
        print("Mi número es más bajo")
    else:
        print(f"Felicidades {nombre}! Has adivinado en {intentos} intentos")
        break
if estimado!= num_secreto:
    print(f"Lo siento {nombre}, se han agotado los intentos. El numero correcto era: {num_secreto}")