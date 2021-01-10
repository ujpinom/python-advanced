##JSON objects are similar to Python dictionaries. Each JSON object contains a commaseparated list of property names and values, in curly braces.
##3{"account": 100, "name": "Jones", "balance": 24.98} Objecto tipo JSON
##JSON also supports arrays which, like Python lists, are comma-separated values in square brackets. [100, 200, 300]

###############------------------------ Python Standard Library Module json-----------------------------------
'''import json;import pandas as pd

libro_cuentas={'Cuentas':[{'cuenta':100,'Nombre':'Uriel','Saldo':23.5},{'cuenta':200,'Nombre':'gato','Saldo':10.3}]}


#------------------------- Serializing an Object to JSON.......................................

with open('accounts.json','w') as cuentas:
    json.dump(libro_cuentas,cuentas)
# ---------------------------------- Deserializing the JSON Text----------------------------------
with open('accounts.json','r') as cuentas:
    cuentas_json=json.load(cuentas)
    print(cuentas_json)

libro_cuentas['Cuentas']+=[{'cuenta':100,'Nombre':'Uriel','Saldo':23.5}]

print(libro_cuentas)'''

#--------------------------------------Handling exceptions-------------------------------------------
#try statement-------------------------

while True:
    try:
        num1= float(input('Ingrese un numero: '))
        num2=float(input('Por favor ingrese otro numero: '))
        result=num1/num2
    except ValueError:
        print('Ingrese valores de tipo numérico.Ingrese un nuevo valor')
    except ZeroDivisionError:
        print('Esta intentando dividir por cero. Ingrese un nuevo valor.')
    else:
        print(f'El resultado de dividir {num1:.2f} entre {num2:.2f} es {result:.2f}')
        break


#----------------------------------- finally Clause------------------------------------------
#A try statement may have a finally clause after any except clauses or the else clause.

###Combining with Statements and try…except Statements----------------------------------------------
try:
    with open('elperronegro.txt','r') as informe:
        print(f'{"Nombre":<5}{"I.D":<7}{"Notas"}')
        for valores in informe:
            nombre,ID,notas= valores.split()
            print(f'{nombre:<5}{ID:<7}{notas}')
except IOError:
    print('No se ha encontrado tal archivo')
