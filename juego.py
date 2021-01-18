import random
import time
import os

def presentacion_1():

    print()
    print("   ****** JUEGO DE LOS PALILLOS ******    ")
    print()
    print()
    print("        Gana quien coge el ultimo palillo   ")
    print()
    print()
    print()
    print(" 1- Facil    /    2- Dificil")
    print()
    print()
    print(" ****************************************** ")
    print()
    
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input(" Elige el nivel 1/2: ")
    return nivel


def presentacion_2(palillos, quitas):

    print()
    print("   ****** JUEGO DE LOS PALILLOS ******    ")
    print()
    print()
    print("        Habra {} palillos en total",format(palillos))     
    print()
    print()
    print()
    print(" se pueden quitar entre 1 y {} palillos", format(quitas))
    print()
    print()
    print("                  Emppiezas a mover tu")
    print()
    print(" *********************************************************")
    entrada= input("press enter")



def sorteo_opciones():
    palillos = random.randint(16,23)
    quitas = random.randint(3,5)

    return palillos, quitas




def area_de_juego(palillos, quitas):

    print()
    print(" ************* Juego de los Palillos ************ ")
    print()
    print()

    for fila in range(4):
        print(end="   ")
        for p in range(1, palillos+1):
            print("|", end="  ")
            if p % quitas == 0: 
                print(end=" ")
        print()
    print()
    print()
    print()


def movimiento_jugador(palillos, quitas):

    if quitas == 3:
        quitas = ("1", "2", "3")
    elif quitas == 4:
        quitas = ("1", "2", "3", "4")
    elif quitas == 5:
        quitas = ("1", "2", "3", "4", "5")
    q = input("  Palitos a quitar : ")
    while q not in quitas or int(q) > palillos:
        if q not in quitas: 
            q = input("Elige entre 1 y {}", format(len(quitas)))
        elif int(q) > palillos: 
            q = input("Solo quedan  {} palillos", format(quitas))
    else:
        palillos_quitar = int(q)

    return palillos_quitar

def movimiento_ordenador_aleatorio(palillos, quitas):
    
    
    palillos_quitar = random.randint(1, quitas)

    while palillos_quitar > palillos:
        palillos_quitar = random.randint(1, quitas)
    
    return palillos_quitar

def  movimiento_ordenador_con_ia(palillos, quitas):

    palillos_quitar = None

    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= quitas:
            palillos_quitar = palillos
        elif palillos % (quitas + 1) == 5:
            palillos_quitar = 5
        elif palillos % (quitas + 1) == 4:
            palillos_quitar = 4
        elif palillos % (quitas + 1) == 3:
            palillos_quitar = 3
        elif palillos % (quitas + 1) == 2:
            palillos_quitar = 2
        elif palillos % (quitas + 1) == 1:
            palillos_quitar = 1
        elif palillos % (quitas + 1) == 0:
            palillos_quitar = random.randint(1,2)
    
    return palillos_quitar


def mostrar_ganador():
    if turno == 2:
        mensaje1 = "   Has ogido el ultimo palillo "
        mensaje2 = "**** Has ganado ****"
    elif turno == 1:
        mensaje1 = "   El ordenador coge el ultimo palillo "
        mensaje2 = "*******    Gana el ordenador    *******"
    
    print()
    print("****** Juego de los palillos ******")
    print()
    print()
    print("{}", format(mensaje1))
    print()
    print("{}", format(mensaje2))
    print()
    print()
    print()


#AHORA ESTABLECEMOS EL PROGRAMA PRINCIPAL 

turno = 1

palillos, quitas = sorteo_opciones()

os.system("cls")
nivel = presentacion_1()

os.system("cls")
presentacion_2(palillos, quitas)


jugando = True

while jugando: 

    os.system("cls")
    area_de_juego(palillos, quitas)

    if turno == 1:
        jugada = movimiento_jugador(palillos, quitas)
        turno = 2
    elif turno == 2: 
        print(" el ordenador esta pensando...")
        time.sleep(2)
        if nivel == "1":
            jugada = movimiento_ordenador_aleatorio(palillos, quitas)
        elif nivel == "2":
            jugada = movimiento_ordenador_con_ia(palillos, quitas)
        turno = 1
    
    
    palillos -= jugada
    
    if palillos == 0:
        os.system("cls")
        mostrar_ganador()
        jugando = False
