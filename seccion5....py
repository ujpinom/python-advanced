#PROGRAMA PARA CALCULAR EL PROMEDIO DE CADA ESTUDIANTES
'''import numpy as np
Estu=int(input('ingrese el numero de estudiantes: '))
Eval=int(input('ingrese el numero de evaluaciones: '))

A=[]
for i in range(1,Estu+1):
    total=0

    print('estudiante numero',i)
    print('---------------')
    for j in range(1,Eval+1):
        print('ingrese la nota #',j,' ',end='')
        nota=float(input(': '))
        total=total+nota
    promedio=total/Eval
    print('el promedio del estudiante numero:',i,'es: ',format(promedio,',.2f'))
    print()
    print()'''

'''for i in range(8):
    for j in range(8):
        if j==i+1:
            print('*'+i*' '+'*',end='')
    print()'''

'''for i in range(8):
    print((8-i)*'*',end='')
    print()'''

import numpy as np
A=[]
for i in range(1,5+1):
    if i==1 or i==5:
        f=1
        A.append(f)
    else:
        A.append(2)
print(A)








