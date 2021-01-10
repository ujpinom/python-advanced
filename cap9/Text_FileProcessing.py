#####################Escribiendo datos en un archivo.txt-----------------------------------------------
import os

with open('Cuentas.txt',mode='w') as cuentas:
    cuentas.write('100 Jones 24.98\n')
    cuentas.write('200 Uriel 23.45\n');cuentas.write('2400 Uriel 23.45\n')

#At the end of the with statement’s suite, the with statement implicitly calls the file object’s close method to close the file.
#--------------------------------------Reading Data from a Text File-----------------------------------------------
with open('Cuentas.txt',mode='r') as cuentas:
    print(f'{"Account":<10}{"Nombre":<10}{"Balance":>10}')
    for datos in cuentas:
        numero_cuenta,nombre,saldo=datos.split()
        print(f'{numero_cuenta:<10}{nombre:<10}{saldo:>10}')

#Updating un archivo existente

input=open('Cuentas.txt','r');temporary_file=open('temporary.txt','w')

with input,temporary_file:
    for archivos in input:
        numero_cuenta,nombre,saldo=archivos.split()
        if numero_cuenta!='2400':
            temporary_file.write(archivos)
        else:
            nueva_entrada=' '.join([numero_cuenta,'Perro','0.0'])
            temporary_file.write(nueva_entrada+'\n')

os.remove('Cuentas.txt');os.rename('temporary.txt','Cuentas.txt')