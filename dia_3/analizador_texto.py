# Ingresar un texto, escoger tres letras, cuantas veces estan las letras en el texto, cuantas palabras hay, 
# cual es la primer y la ultima letra, palabras en orden reverso, python esta en el texto?

#Se ingresa el texto para analizar
texto= input("Ingresa el texto a analizar: ")

#se inicia la variable donde se guardaran las letras  a buscar
letras= []

#se pasa todo el texto a minusculas, por si incluyeron mayusculas
texto= texto.lower()
print("\n")
#se agregan las variables a buscar en el texto a la varibale letras
letras.append(input("ingrese la primer letra a buscar: ").lower())
letras.append(input("ingrese la segunda letra a buscar: ").lower())
letras.append(input("ingrese la tercer letra a buscar: ").lower())

print("\n")
print("Cantidad de letras ")
cantidad_letras1= texto.count(letras[0])
cantidad_letras2= texto.count(letras[1])
cantidad_letras3= texto.count(letras[2])

print(f"Hemos encontrado la letras '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letras '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letras '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras ")

palabras=texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("Letras de inicio y de fin ")

letra_inicial = texto[0]
letra_final = texto[-1]

print(f"La letra inicial es: '{letra_inicial}' y la letra final es '{letra_final}' ")

print("\n")
print("Texto invertido ")

palabras.reverse()
texto_invertido = ' '.join(palabras)

print(f"Si ordenamos tu texto al reves va a decir: '{texto_invertido}'")

print("\n")
print("Buscando la palabra python ")

buscar_python = 'python' in texto

dic={ True: "sí", False:"no"}

print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")