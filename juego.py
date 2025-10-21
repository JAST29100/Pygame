import random as al
import time
import os
import sys

# La funcion nl imprime una linea vacia en la consola
def nl():
    print()
# La funcion cls limpia la pantalla de la consola
def cls():
    os.system("cls" if os.name == "nt" else "clear")
# La funcion Decision permite pedirle al usuario que ingrese una opcion numerica dentro de un rango dado por "opciones"
def Decision(opciones):
    posibles = list(range(1, opciones + 1))
    while True:
        entrada = int(input("> "))
        if entrada in posibles:
            return entrada
        else:
            sys.stdout.write("\033[F\033[K")
# La funcion InicializarEstadisticas inicializa las estadisticas del jugador
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
# La funcion MenuInicio muestra el menu de inicio del juego
def MenuInicio():
    cls()
    print("""=================================
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
        print("""===========================
       ACERCA DEL JUEGO
===========================
El Juego es una aventura roguelite narrativa
que mezcla misterio psicologico con la emocion de las apuestas.

Despiertas en un bar tenuemente iluminado, sin memoria
de quien eres ni de cómo llegaste ahi. Desde ese momento,
cada decision cuenta.

Explora encuentros extraños, administra tus recursos
y equilibra tu cordura mientras descubres fragmentos
de tu pasado olvidado.

El oro, la salud, la suerte y la reputación daran forma
a tu viaje a través de este mundo de caos y apuestas.

Preparate para una atmosfera inquietante, eventos inesperados
y una constante sensacion de incertidumbre.
¿Descubrirás la verdad... o te perderas en el intento?

> Presiona Enter para regresar al menu principal.
""")
        input()
        MenuInicio()
    if opcion == 3:
        cls()
        print("""===============================
   ACERCA DE LOS DESARROLLADORES
===============================

Este proyecto fue creado por:

• Joseph Andrés Salazar Tobón
• Carlos Eduardo Rojas

Desarrollado como parte de una clase universitaria de programacion y algoritmos,
este juego representa la nota final para nuestra clase (y tambien nuestro amor por los juegos).

Queriamos mezclar el rpg y el azar para crear un mundo
que se sintiera vivo, impredecible y un poco inestable.

Hecho en Python, con vibes positivas y muchas busquedas en Google.

> Presiona Enter para regresar al menu principal.
""")
        input()
        MenuInicio()
# La funcion MensajeInicio muestra el mensaje inicial del juego, introduce un poco el lore.
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

# ============================== Funcion principal ==============================
def main():
    cls()
    oro, limite_salud, salud, suerte, limite_mp, mp, reputacion, cordura = InicializarEstadisticas()
    MensajeInicio()

# ============================== Inicio del juego ==============================
if __name__ == "__main__":
    MenuInicio()