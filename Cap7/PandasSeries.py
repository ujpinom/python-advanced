import pandas as pd
import numpy as np

grades=pd.Series([1,2,4.6,67])
print(grades)
arreglo1=pd.Series(98,range(10));print(arreglo1) #Crea una Serie de pandas donde el primer elemento indica el valor con el cual se rellena la serie y el segundo argumento indica los indices
arreglo2=pd.Series(34,[0,1,3,4,5,7]);print(arreglo2,arreglo2.count())
print(grades.describe())
#Si se crea una serie con un diccionario, las claves se convierten en indices de los valores:
notas_estudiantes=pd.Series({'Perro':[1,2,3,4],'gato':[3,4,5,6,7]});print(notas_estudiantes['Perro'])
print(notas_estudiantes)
notas_estudiantes2=pd.Series([[1,2,4],[4,5,6],[6,7,3]],index=['urrao','ere','ersd']) # Otra forma de crear Series
print(notas_estudiantes2);print(notas_estudiantes2.values)
nombres=pd.Series(['toro','caballo','ggato','perro'])
aa= np.array(nombres.str.contains('a').values)
print(aa);print(nombres.str.upper())