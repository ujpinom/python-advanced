import numpy as np;import pandas as pd
pd.set_option('precision', 2)##Fija el numero de decimales a imprimir
directorio_notoas={'Uriel':[87, 96, 70],'Pacgo':[100, 87, 90],'Sam': [94, 77, 90], 'Katie': [100, 81, 82],'Bob': [83, 65, 85]}

notas= pd.DataFrame(directorio_notoas);print(notas)  #En dataFrames cada serie se convierte en columna. Keys se convierten en el nombre de las columnas
print(notas.values)
#los indices de las filas se pueden personalizar al momento de crear el DataFrame
notas=pd.DataFrame(directorio_notoas,index=['Prueba1','Prueba2','Prueba3']);print(notas);print(notas['Sam'])#Imprime las notas de Sam en forma de serie

#-----------------------------------Selecting Rows via the loc and iloc Attributes----------------------------------------------
#You can access a row by its label via the DataFrame’s loc attribute.
print(notas.loc['Prueba2']) #Imprime la columna 'Prueba2' en forma de serie, cuyos indices son los nombres de las columas del DataFrame
#   You can access a row by its label via the DataFrame’s loc attribute.
print(notas.iloc[2]) #Imprime una serie la cual contiene el resultado de las notas en la fila 2;

#____________________________________________________________---Selecting Rows via Slices and Lists with the loc and iloc Attributes-----------------

print(notas.loc['Prueba1':'Prueba2']);print(notas.iloc[1:3,0:4])

#To select specific rows, use a list rather than slice notation with loc or iloc:
print(notas.loc[['Prueba1','Prueba3']])

#******************************************************** Boolean Indexing+++++++++++++++++++++++++++++
print(notas[notas>=90]) #Retorna las notas que son iguales o superiores al valor especificado
#Let’s select all the B grades in the range 80–89:
print(notas[(notas>=80) & (notas<90)])
#*************************************+Accessing a Specific DataFrame Cell by Row and Column++++++++++++++++++++++++++
print(notas.at['Prueba1','Uriel'])
notas.at['Prueba1','Uriel']=100 #Cambia la nota de la prueba1 para el estudiate Uriel a un nuevo valor de 100
notas.iat[0,4]=100 # Utilizando numeros enteros
resumen=notas.describe()
print(notas);print(notas.describe());print(resumen.loc['mean',:]);print(notas.mean());print(notas.T)
print(notas.T.mean())#Traspone los datos convirtiendo filas en columnas y viceversa. Adicionalmente retorna la media  de todos los estudiates para cada prueba

#++++++++++++++++++++++++++++++Sorting by Column Indices+++++++++++++++++++++++++++++++++++
#Para organizar los indices de las columas debemos especifica axis=1; si se quiere ordenar por indices de las filas axis=0
print(notas.sort_index(axis=1));print(notas.sort_index(axis=0,ascending=False,inplace=True
                                                       ));



