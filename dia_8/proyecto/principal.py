import numeros

def preguntar():

    print("\nBienvenido a farmacia Python")


    while True:
        print("[P] - Perfumeria \n[F] - Farmacia \n[C]- Cometologia")
        try:
            ubicacion= input("Elige la tienda que quieres visitar: ").upper()
            ["P","F","C"].index(ubicacion)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break
    
    numeros.decorar_turno(ubicacion)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("\nQuieres sacar otro turno [S] [N]: ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("\nEsa no es una opcion valida")
        else:
            if otro_turno =="N":
                print("\n" + "*" * 23)
                print("\nGracias por su visita")
                break

inicio()