'''max_temp=102.5
#Llamar funciones dentro de un ciclo while
def main():
    masdatos='y'
    while masdatos=='y':
        comisiones()
        masdatos = input('desea ingresar mas datos?Si es así ingrese "y" como respuesta afirmativa:')
def comisiones():
    VENTAS=float(input('Ingrese el numero de ventas:'))
    precio=float(input('Ingrese el valor de la comision:'))
    comissiones=VENTAS*precio
    print('Las comisiones son:',comissiones)

main()'''

'''def sumaa():
    suma=0
    print('impares\tpares') #crea tablas
    print('-----------------')
    for i in [1,2,3,4,5,6,7,8,9]:
        if i%2==0:
            print(i,'   ',sep='') #imprime los numeros en formato vertical
        else:
            print(i, ' ',end='      ')  #imprime los numeros en formato horizontal
        suma += i

    print()
    print()
    print('y la suma de todos los numeros es:',suma)

sumaa()'''

'''Vel_min=int(round(float(input('ingrese la velocidad minima'))))
Vel_max=int(input('ingrese la velocidad maxima'))
while Vel_max<0 or Vel_min<0:
    print('Las velocidades son magnitudes.Debe ingresar un número positivo')
    Vel_min = int(input('ingrese la velocidad minima'))
    Vel_max = int(input('ingrese la velocidad maxima'))
print('Tabla de conversion kmh a mph')
print('KMH \t MPH')
print('-------------------')
for KMH in range(Vel_min,Vel_max,10):
    MPH=KMH*0.6214
    print(KMH,'  \t',format(MPH,'.2f'))'''
'''import numpy as np
A=[]

producto=0
while producto<100:
    num=float(input('ingrese un numero: '))
    producto=num*10
    A.append(producto)

    #print(A,' ',end='')
print(producto)
print(A)''' # Hay información sobre como guardar información en vectores y matrices(Listas)
'''Ter_serie=int(input('Ingrese el numero de terminos de la serie: '))
suma=0
for i in range(1,Ter_serie+1):
    suma+=i/((Ter_serie+1)-i)
    print(format(i/((Ter_serie+1)-i),',.4f'))
print()
print('La suma total de cada uno de los terminos de la serie es: ',format(suma,',.3f'))'''
# This program has two functions. First we
# define the main function.
'''def main():
    print('Pasos para desarmar una lavadora')
    print('Acontinuación encontrará los pasos que debe seguir para llevar a cabo el correcto desmonte'
          'de la lavadora')
    input('presione enter para conocer el paso 1:')
    print()
    paso1()
    input('presione enter para conocer el paso 2:')
    print()
    paso2()
    input('presione enter para conocer el paso 3:')
    print()
    paso3()
    input('presione enter para conocer el paso 4:')
    print()
    paso4()
    print()
    print('Felicidades ha desmontado correctamente la lavadora')

def paso1():
    print('desconecte la lavadora y jalela hacia atras')
def paso2():
    print('retire cada uno de los tornillos que tiene la lavadora en la parte de atras')
def paso3():
    print('retire la cubierta metalica para poder acceder a los componentes internos')
def paso4():
    print('Verifique los componentes. Si observa algo que este en mal estado o quemado, por favor lleve el producto '
          'a un centro de servicios')

main()'''

def main():
    print('{:^100}'.format('Vamos a calcular el voltaje por medio de la ley de ohm'))
    print()
    Resitencia=3.5
    Corriente=5
    ley_ohm(resistencia=Resitencia,corriente=Corriente)
def ley_ohm(corriente,resistencia):
    voltaje=resistencia*corriente
    print('El voltaje para los valores ingresados es: ',voltaje,'voltios')
main()



