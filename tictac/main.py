import math
import random

import numpy as np

class player ():


    def __init__(self):

        self.coordenadas ={}

        self.victorias =0

        self.ganador = False

        self.nombre = ''

        self.maquina = False



class tablero():

    def __init__(self, dimension):

        self.dimensiones =  dimension

        self.tablero = np.full((dimension, dimension), '*')

        self. jugadas = []  # vector con objetos de tipo player

        self.ganador = False

        self.tablero_lleno = False

    def imprimir_tablero(self):

        for i in range (len(self.tablero)):

            for j in range ( len (self.tablero)):

                print(self.tablero[i][j], sep='   ', end='    ')

            print()
            print()


    def validar_movimiento(self, jugador):

        x = jugador.coordenadas['x']
        y = jugador.coordenadas['y']


        if ((x < 0 or  x> self.dimensiones-1) or (y < 0 or  y> self.dimensiones-1)):

            return 'OUT'

        elif (self.tablero[x][y] != '*'):

            return 'OCU'
        else:
            return 'VALID'


    def ganador_tablero_lleno(self, jugador):

        x = jugador.coordenadas['x']
        y = jugador.coordenadas['y']




        if x == y or x + y == self.dimensiones - 1:

            self.validar_diagonal()

        fila =np.unique(self.tablero[x,:])

        col = np.unique(self.tablero[:,y])

        if  len(fila) ==1 and fila[0] !='*':

            self.ganador = True

        if len(col) == 1 and col[0] != '*':
            self.ganador = True

        if '*' not in self.tablero and self.dimensiones>1 :
             self.tablero_lleno= True



    def validar_diagonal(self):

        diag_principal = np.unique(np.diag(self.tablero))

        diag_sec = np.unique(np.fliplr(self.tablero).diagonal())

        if len(diag_principal) ==1 and diag_principal[0] != '*':

            self.ganador=True

        if len(diag_sec) == 1 and diag_sec[0] != '*':
            self.ganador = True


def jugada(jugador,dimension, tablero):

    if jugador.maquina:

        posicion= random.randint(0, dimension*dimension-1)

        while True:

            posicion = int(posicion)
            x = math.floor(posicion / dimension)
            y = posicion % dimension
            jugador.coordenadas['x'] = x
            jugador.coordenadas['y'] = y

            movimiento = tablero.validar_movimiento(jugador)

            if movimiento == 'VALID':
                tablero.tablero[x][y]= 'M'
                break

            posicion = random.randint(0, dimension * dimension - 1)

        print(f'La jugada de la maquina es : {posicion}')

    else:
        print(f'Ingrese la posicion. Numero entre 0 y {dimension*dimension-1}')

        posicion = input()

        while True:

            if posicion.isnumeric():

                posicion = int (posicion)
                x= math.floor(posicion / dimension)
                y =  posicion % dimension
                jugador.coordenadas['x']=x
                jugador.coordenadas['y']=y



                movimiento = tablero.validar_movimiento(jugador)
                if movimiento == 'OUT':
                    print('Coordenadas fuera de las dimensiones')

                if movimiento == 'OCU':

                    print('Posicion ya ocupada')


                if movimiento == 'VALID':
                    tablero.tablero[x][y]= 'P'
                    break
            print(f'Ingrese la posicion. Numero entre 0 y {dimension * dimension - 1}')

            posicion = input()



nuevo_juego = 'y'

p2 = player()
p1 = player()

while nuevo_juego == 'y':
    print('Ingrese las dimensiones del tablero: ')
    try:
        dimension = int(input())
    except ValueError:
        print('El valor ingresado no es un numero')

    juego = tablero(dimension)

    print('Seleccione su turno: primero o segundo ?')

    turno_jugador = int(int(input())%2)

    p1.maquina=False
    p2.maquina=False

    if turno_jugador == 1 :
        p2.maquina= True
        p2.nombre='La maquina'
        p1.nombre = 'Yo perro'

    else:
        p1.maquina= True
        p1.nombre = 'La maquina'
        p2.nombre = 'Yo perro'

    orden_players = [p1, p2]

    while (not juego.ganador) and (not juego.tablero_lleno):

        for p in orden_players:

            jugada(p,dimension,juego)

            juego.ganador_tablero_lleno(p)

            juego.imprimir_tablero()


            if juego.ganador:

                p.victorias+=1

                print(f'El ganador ha sido: {p.nombre}')

                break

            if juego.tablero_lleno:
                print('El tablero esta lleno....')
                break

            print('Presione ENTER para seguir con la proxima jugada')

            input()



    print('El juego termino. Desea seguir jugando? y/n')

    nuevo_juego = str(input()).lower()

print(f'El jugador {p1.nombre} tuvo {p1.victorias} victorias')
print(f'El jugador {p2.nombre} tuvo {p2.victorias} victorias')
print('Muchas gracias por jugar nuestro juego. Adios')

