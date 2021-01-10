import pandas as pd
import csv
from matplotlib import  pyplot as pyp

with open('accounts.csv','w',newline='') as cuentas:
    hola_perro=csv.writer(cuentas)
    hola_perro.writerow([100,'Jones',24.98]) #writerow() en su argumento recibe un iterable
    hola_perro.writerow([200, 'Doe', 345.67])
    hola_perro.writerow([300, 'White', 0.00])
    hola_perro.writerow([400, 'Stone', -42.16])
    hola_perro.writerow([500, 'Rich', 224.62])

    #The csv module’s writer function returns an object that writes CSV data to the specified file object.

#-------------------- Reading from a CSV File----------------------------------------------


with open('accounts.csv','r',newline='') as cuentas:
    print(f'{"Codigo":<10}{"Nombre":<10}{"Saldo":<10}')
    cuentas= csv.reader(cuentas)
    for datos in cuentas:
        codigo,nombre,saldo=datos #retorna una lista la cual se unpack en codigo,nombre,saldo
        print(f'{codigo:<10}{nombre:<10}{saldo:<10}')



####------------------------- Working with Locally Stored CSV Files----------------------------------
#You can load a CSV dataset into a DataFrame with the pandas function read_csv.
df=pd.read_csv('accounts.csv',names=['Codigo','Nombre','Saldo'])
print(df)
#To save a DataFrame to a file using CSV format, call DataFrame method to_csv:
df.to_csv('cuentas_from_df.csv',index=False)##The index=False keyword argument indicates that the row names (0–4 at the left of the DataFrame’s output in snippet [3]) are not written to the file.

#------------------------------------------ Reading the Titanic Disaster Dataset------------------------------------------------------------
pd.set_option('precision',2) # format for floating-point values
titanic_datas= pd.read_csv('C:\\Users\\SONY\\Desktop\\transporte\\TitanicSurvival.csv')
titanic_datas.columns=['Nombre','Sobrevivió','Genero','Edad','Clase'] #Cambiar el nombre de cada una de las columnas por los valores especificados

titanic_datas.head()
print(titanic_datas);print(len(titanic_datas))
print((titanic_datas.Clase=='1st').describe())
histo=titanic_datas.hist()
pyp.xlabel('Distribución edades');pyp.ylabel('Nro.Pasajeros')
pyp.show()

#Now, you can use pandas to perform some simple analysis. For example, let’s look at some descriptive statistics.
#---------------------------------------------- Passenger Age Histogram----------------------------------------------
