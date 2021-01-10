from matplotlib import animation
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import random;import numpy as np


def actualizacion(numero_cuadros,numero_tiros,caras,frecuencia):
    titulo = f'Lanzando un dado de 6 caras {sum(frecuencia):,} de veces'
    for i in range(numero_tiros):
        frecuencia[random.randrange(1,7)-1]+=1

    plt.cla()
    top=max(frecuencia)
    ejes = sns.barplot(x=caras, y=frecuencia, palette='bright')
    plt.title(titulo)
    plt.xlabel('Cara')
    plt.ylabel('Frecuencia')
    plt.ylim(top=max(frecuencia)*1.10)


    for bar,frec in zip(ejes.patches,frecuencia):
        text_x=bar.get_x()+bar.get_width() / 2.0
        text_y=bar.get_height()
        txt = f'{frec}'
        ejes.text(text_x,text_y,txt,fontsize=11, ha='center', va='bottom')



numero_cuadros=int(input('Por favor ingrese el numero de cuadros:'))
numero_tiros= int(input('Por favor ingrese el número de tiros por cuadro: '))
sns.set_style('whitegrid')
figure = plt.figure('Rolling a Six-Sided Die')
caras=list(range(1,7))
frecuencia= [0] * len(caras)

animation_dados=animation.FuncAnimation(figure,actualizacion,repeat=False,frames=numero_cuadros,interval=33,
                                        fargs=(numero_tiros,caras,frecuencia))
plt.show()

