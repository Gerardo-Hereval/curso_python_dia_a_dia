# class Casa:
#     def __init__(self,color,cantidad_pisos):
#         self.color=color
#         self.cantidad_pisos=cantidad_pisos
#
# casa_blanca=Casa("blanco",4)
#
# class Cubo:
#     caras=6
#
#     def __init__(self,color):
#         self.color=color
#
# cubo_rojo=Cubo('rojo')
#
#
# class Personaje:
#     real=False
#     def __init__(self,especie,magico,edad):
#         self.especie=especie
#         self.magico=magico
#         self.edad=edad
#
# harry_potter=Personaje("Humano",True,17)

# class Pajaro:
#
#     alas= True
#
#     def __init__(self,color,especie):
#         self.color = color
#         self.especie = especie
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color)) #debemos poner format y decirle a quien se refiere con self
#     def volar(self,metros):
#         print(f"El pajaro ha volado {metros} metros")


# class Perro:
#     def ladrar(self):
#         print("Guau!")
#
# class Mago:
#     def lanzar_hechizo(self):
#         print("¡Abracadabra!")
# merlin=Mago()
#
# class Alarma:
#     def postergar(self,cantidad_minutos):
#         print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

# class Pajaro:
#
#     alas= True
#
#     def __init__(self,color,especie):
#         self.color = color
#         self.especie = especie
#     def piar(self):
#         print('pio, mi color es {}'.format(self.color)) #debemos poner format y decirle a quien se refiere con self
#     def volar(self,metros):
#         print(f"El pajaro ha volado {metros} metros")
#     def pintar_negro(self):
#         self.color='negro'
#         print(f"Ahora el pajaro es {self.color}")
#     @classmethod
#     def poner_huevos(cls,cantidad):
#         print(f"Puso {cantidad} huevos")
#         cls.alas=False
#         print(Pajaro.alas)
#     @staticmethod
#     def mirar():
#         print("el pajaro mira")
#

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar...Exhalar")

class Jugador:
    vivo=False
    @classmethod
    def revivir(cls):
        cls.vivo=True

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1


class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

cosas=[palabra,lista,tupla]

for i in cosas:
    print(len(i))


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


a = Arquero()
m = Mago()
s = Samurai()

personajes = [a, m, s]

for personaje in personajes:
    personaje.atacar()