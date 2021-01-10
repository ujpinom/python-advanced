import numpy as np;import pandas as pd
import seaborn; from matplotlib import pyplot as pyp
from scipy import stats
##Relaciones lineales; convirtiendo temperaturas de farenheit a celcius
def tempe():
    c=lambda f:5/9*(f-32)
    temperaturas=[(f,c(f)) for f in range(0,101,5)]
    tempe_df=pd.DataFrame(temperaturas,columns=['Fahrenheit','Celcius'])
    axes= tempe_df.plot(x='Fahrenheit',y='Celcius',style='.-')
    pyp.ylabel('Celcius');pyp.title('Relacion entre F y C')
    pyp.show()



def nyc_temperaturas():
    c=lambda f:5/9*(f-32)

    nyc_temp=pd.read_csv('C:\\Users\SONY\\Desktop\\transporte\\USH00305801-tmax-1-1-1895-2020.csv')#importa un archivo tipo
    #CSV a un DataFrame de pandas


    ##--------------------- Cleaning the data----------------------
    nyc_temp.columns=['Fecha','Temperatura','Anomalía']
    tempe_celcius= [c(f) for f in nyc_temp.Temperatura]
    nyc_temp.Temperatura=pd.Series(tempe_celcius)
    nyc_temp.Fecha=nyc_temp.Fecha//100

    #------------------ Forecasting Future January Average High Temperatures----------------------
    regresion_lineal= stats.linregress(x=nyc_temp.Fecha,y=nyc_temp.Temperatura)
    print(regresion_lineal)

    seaborn.set_style('whitegrid')
    axes= seaborn.regplot(x=nyc_temp.Fecha,y=nyc_temp.Temperatura);
    pyp.ylabel('Grados Celsius')
    pyp.show(),

nyc_temperaturas()