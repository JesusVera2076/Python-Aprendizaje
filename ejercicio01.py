#TRABAJO PRÁCTICO N°3 - CASANOVA, BONESSO, VERA, GONZALEZ
#COM. 109 Y 107

#LIBRERIAS
import time 
import os 
import os.path
import pickle 
from colorama import init, Fore
import time 
import random
import pwinput 

#funcion para avisar que un modulo esta en construccion
def cartel():
    print(Fore.RED+"...en construcción...")

#funcion para limpiar la pantalla
def limpiar_pantalla():
    pantalla = os.name  
    if pantalla == 'nt':
        os.system('cls')

def titulo(texto):
    print(Fore.CYAN + "╔══════════════════════════════════════════════╗")
    print(Fore.CYAN +f"║{texto:^46}                                   ║")
    print(Fore.CYAN + "╚══════════════════════════════════════════════╝")


def cuadro_resultado(titulo, jugador, mensaje):
    print(Fore.YELLOW + "╔══════════════════════════════════════════════╗")
    print(Fore.YELLOW +f"║{titulo:^46}                                  ║")
    print(Fore.YELLOW + "╠══════════════════════════════════════════════╣")
    print(Fore.WHITE + f"║ Jugador: {jugador:<35}                       ║")
    print(Fore.WHITE + f"║ {mensaje:<44}                                ║")
    print(Fore.YELLOW + "╚══════════════════════════════════════════════╝")


def cartel_ganador():
    print(Fore.GREEN + "╔════════════════════════════╗")
    print(Fore.GREEN + "║         ¡GANASTE!          ║")
    print(Fore.GREEN + "╚════════════════════════════╝")


def cartel_perdedor():
    print(Fore.RED + "╔════════════════════════════╗")
    print(Fore.RED + "║         PERDISTE           ║")
    print(Fore.RED + "╚════════════════════════════╝")
