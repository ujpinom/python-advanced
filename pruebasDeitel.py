import random
import math
import statistics as stats

def Craps():

    numero=roll_dice() #obtiene la suma
    scope=numero
    if(numero==7 or numero==11):
        print('Ha sacado un: ',numero)
        print('Felicidades ha ganado en la primera jugada')
    elif( numero==2 or numero==3 or numero==12):
        print('Ha sacado un: ', numero)
        print('Usted acaba de perder en el primer tiro. Mala suerte')
    else:
        print('Ha sacado un: ', numero)
        print('Usted continua en el juego, debe sacar un ',scope, 'para ganar. Recuerde que perderá si saca un 7')

        numero=roll_dice()

        bandera=True
        contador=2
        while(numero !=scope):
            contador+=1
            print('Ha sacado un: ', numero)
            if(numero==7):
                print('Es una lastima usted ha perdido')
                bandera=False
                break
            else:
                numero=roll_dice()
        if(bandera):
            print('Ha sacado un: ', numero)
            print('Por fin ha ganado despues de',contador,' tiros. Ese, ',scope,' le otorgó la victoria')

def roll_dice():
    """Retorna la suma de dos dados"""
    return random.randrange(1,7)+random.randrange(1,7)



def average(*argumentos):
    if(len(argumentos)==0):
        return 'Debe pasar al menos 1 argumento para calcular el promedio'
    else:
        return sum(argumentos)/len(argumentos)


g=[88, 75, 96, 55, 83]

print('promedio de',g,'es',average(*g))