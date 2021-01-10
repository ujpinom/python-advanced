#factorial
#ef pas():
#import numpy as np
pascal=int(input('Ingrese el numero de filas del triangulo de pascal: '))

A=[]
B=[]
for i in range(1,pascal+1):
    if i==1:
        aa=[[1]]
        B=B+aa
        print([1])
    elif i==2:

        bb=[1,1]
        cc=[[1,1]]
            #print([i-1,i-1])
        A=bb
        B=B+cc
        print(A)
    elif i>2:
        C=[]
        D=[C]

        for k in range(1,i+1):
            if k==1 or k==i:
                C.append(1)
            else:
                f=A[k-2]+A[k-1]
                C.append(f)
        A=C
        B=B+D
        print(C)

print('¿quiere tener acceso a alguna de las lineas? Ingrese "si" si a si lo desea entre otro valor si quiere lo contrario')
control=input('Ingrese su respuesta: ')
while control=='si':
    print('A que fila del triangulo de pascal quiere tener acceso')
    fila=int(input(': '))
    while fila<0 or fila>pascal:
        print('Ingrese una fila correcta. El triangulo que usted ingreso solo tiene',pascal,'filas')
        fila=int(input(': '))
    print('La fila deseada del triangulo de pascal es: ',B[fila-1])
    print()
    control=input('Desea conocer el valor de alguna otra fila? Entre "si o no": ')
    print()
print('adios')








