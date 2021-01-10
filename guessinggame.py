print('{:^100}'.format('Welcome to the guessing game'))
print('Este es un juego de adivinación. Aleatoriamente se generará un numero en el intervalo del 1 al 10')
print('Tiene un maximo de 4 oportunidades para acertar, de lo contrario perderá el juego.Buena suerte')
print()

import random
def game():
    jugar='si'
    A=[]
    while jugar=='si':
        number_to_guess = random.randint(1, 10)
        print(number_to_guess)
        user_entrada = int(input('Ingrese un numero para adivinar en el intervalo 1 a 10:'))

        count = 1
        while user_entrada != number_to_guess and count<4:
            diff=number_to_guess-user_entrada
            if user_entrada>10 or user_entrada<1:
                print('El  numero ingresado no esta dentro del intervalo permitido')
                count=count-1
            else:
                if diff>0:
                    print('El numero ingresado es menor que el numero a adivinar')
                    print('tiene', 4 - count, 'oportunidades')
                elif diff<0:
                    print('el numero ingresado es mayor que el numero a adivinar')
                    print('tiene', 4 - count, 'oportunidades')
            print()
            #print('tiene', 4 - count, 'oportunidades')
            print()
            count += 1
            user_entrada=int(input('Ingrese el nuevo numero: '))
        if count<=4 and user_entrada == number_to_guess :
            print('Felicidades! You have won. Te tomó',count,'intentos para completar el juego')
        else:
            print('you have lost')
            print('El numero correcto es:',number_to_guess)
            count+=1

        A.append(count)
        jugar=input('Deseaas seguir jugando? Ingrese "si" si asi lo desea: ')
    print(A)
    main(A)
    print()

def main(A):
    print('A continuación vamos a conocer los resultados de las personas que participaron en el juego')

    for persona in range(1,len(A)+1):
        if A[persona-1]<5:
            print('La persona',persona,'gano con',A[persona-1],'intentos',' ',end='')
        else:
            print('La persona',persona,'no pudo completar el juego',' ',end='')
        print()


game()

