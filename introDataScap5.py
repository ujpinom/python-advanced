import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import random;import numpy as np

def frecuencia_cara_dados(x):
    tiros= [random.randrange(1,7) for i in range(x)]

    valores,frecuencia=np.unique(tiros,return_counts=True)
    print(valores)
    titulo= f'Lanzando un dado de 6 caras {len(tiros):,} de veces'
    sns.set_style('whitegrid');
    ejes=sns.barplot(x=valores,y=frecuencia,palette='bright')
    plt.title(titulo)
    plt.xlabel('Cara')
    plt.ylabel('Frecuencia')
    plt.ylim(top=max(frecuencia) * 1.10)

    for barra,f in zip(ejes.patches,frecuencia):
        text_x=barra.get_x()+barra.get_width() / 2.0
        text_y=barra.get_height()
        txt=f'{f}'
        ejes.text(text_x, text_y, txt, fontsize=11, ha='center', va='bottom')


    '''for bar in range(len(ejes.patches)):

        text_x = ejes.patches[bar].get_x() + ejes.patches[bar].get_width() / 2.0
        text_y = ejes.patches[bar].get_height()
        texto = f'{frecuencia[bar]:,}'
        ejes.text(text_x, text_y, texto, fontsize=11, ha='center', va='bottom')'''

    plt.show()

x=int(input('Por favor ingres el numero de veces que deses arrojar el dado: '))
frecuencia_cara_dados(x)