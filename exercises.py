import math
def main():
    #Pago=sales * commission rate + advanced pay
    ventas= get_ventas()
    rate=get_rate(ventas)
    advanced_pay=get_advanced()

    pago=ventas*rate-advanced_pay
    if(pago<0):
        print('El empleado debe retornar a la empresa un valor de: ',math.fabs(pago))
    else:
        print('El salario neto del empleado es : ',pago)

def get_advanced():
    hola= float(input('Puede acceder a un adelanto de su sueldo. Introduzca un valor entre 0 y 2000: '))
    while(hola<0 or hola>2000):
        print('Valor no permitido. Ingrese un nuevo valor')
        hola=float(input(':'))
    return hola


def get_ventas():
    return float(input('Ingrese sus ventas: '))
def get_rate(ventas):
    if(ventas<10000):
        return 0.1
    elif(ventas>=10000 and ventas <15000):
        return 0.12
    elif(ventas>=15000 and ventas <18000):
        return 0.14
    elif(ventas>=18000 and ventas <22000):
        return 0.16
    else:
        return 0.18



def main2():

    num1= 19
    if(isEven(num1)):{
        print('El numero ingresado es par')
    }
    else:{
        print('El numero no es par')
    }
def isEven(num1):

    if((num1%2)==0):
        return True
    else:
        return False

main2()

print(51/13)