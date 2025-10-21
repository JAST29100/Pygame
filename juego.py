import random as al
import time
import os
import sys

def nl():
    print()

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def Decision(opciones):
    posibles = list(range(1, opciones + 1))
    while True:
        entrada = int(input("> "))
        if entrada in posibles:
            return entrada
        else:
            sys.stdout.write("\033[F\033[K")

def InicializarEstadisticas():
    oro = 100
    limite_salud = 100
    salud = 10
    suerte = 0
    limite_mp = 0
    mp = 0
    reputacion = "Desconocido"
    cordura = "Desvaneciéndose..."
    return oro, limite_salud, salud, suerte, limite_mp, mp, reputacion, cordura

def MenuInicio():
    cls()
    print(
"""=================================
     BIENVENIDO AL JUEGO
=================================
1. Empezar a jugar
2. Acerca del juego
3. Acerca de los desarrolladores
""")
    opcion = Decision(3)
    if opcion == 1:
        cls()
        print("¡Esperamos que disfrutes el juego y buena suerte, la vas a necesitar!")
        time.sleep(2)
        main()
    if opcion == 2:
        cls()
        print()
        input()
        MenuInicio()
    if opcion == 3:
        cls()
        print()
        input()
        MenuInicio()

def MensajeInicio():
    print("Acabas de despertar. Miras a tu alrededor y te encuentras en medio de un bar.")
    time.sleep(3)
    print("Intentas recordar que paso y donde estas.")
    input()
    print("...")
    time.sleep(1.5)
    print("....")
    time.sleep(1.5)
    print(".....")
    time.sleep(1.5)
    print("\nNo puedes recordar absolutamente nada. Ni siquiera tu nombre.")
    time.sleep(3)
    print("Confundido, te levantas y buscas a la persona mas cercana para preguntar donde estás.")
    input()
    cls()

def main():
    cls()
    oro, limite_salud, salud, suerte, limite_mp, mp, reputacion, cordura = InicializarEstadisticas()
    MensajeInicio()

if __name__ == "__main__":
    MenuInicio()
