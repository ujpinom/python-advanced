from collections import Counter


#---------------------------------------Diccionarios----------------------------------------------

'''diccionario={'perro':'p','gato':'g','vaca':'v'}
if diccionario:
    print('El diccionario tiene elementos')

diccionario.clear()  #El metodo clear borra los elementos del diccionario
print(diccionario)

meses={'enero':31,'febreo':28,'marzo':31}
if 'enero' in meses:  #Pregunta si la clave esta en el diccionario
    print('Claro que si perro')
    print(meses['enero']) # retorna el valor asignado para la clave enero
    meses['enero']+=1   # Actualiza el valor para la clave enero

for keys,values in meses.items():  #items() retorna una tupla consitente de la clave y el valor
    print(f'El mes {keys} tiene {values} días')

meses['Mayo']=31;  #Agregando un nuevo elemento al diccionario
print(meses)
del meses['Mayo'] #Elimina el par key-value especificado del diccionario
print(meses)
#Una forma alternativa de borrar un elemento del diccionario es usando el metodo pop(key)
meses['Mayo']=31;
print(meses);meses.pop('Mayo');print(meses)

#otra forma de obtener el valor de una key es usando el metodo .get(key)
#se puede iterar a traves de solo las claves o los valores usando los metodos .keys() o .values() respectivamente  ver pagina 142-143 del libro

lista_meses= list(meses.keys())
print(lista_meses)'''  #Alguno metodos de los diccionarios

'''def nota_estudiante():

    libro_notas={'Uriel':[92, 85, 100],
                 'Perro':[83, 95, 79],
                 'Gato':[91, 89, 82],
                 'El gono':[97, 91, 92]}

    promedio_clase=0

    for estudiante,calificaciones in libro_notas.items():
        total=sum(calificaciones)
        propemedio=total/len(calificaciones)
        promedio_clase += propemedio
        print(f'El promedio para el estudiante {estudiante} es {propemedio:.2f}')

    print(f'El promedio para la clase es: {promedio_clase/len(list(libro_notas.keys())):.2f}')


nota_estudiante()''' #Registrando en diccionarios las notas de estudiantes
def contador_palabras():

    saludo='Hola perro gonorrea Espero que la haya pasado mal gonorrea'

    contador_palabras={}

    print(f'{"Word":<12}Cuenta')
    for token in saludo.lower().split():

         if( token in contador_palabras):
             contador_palabras[token] += 1
         else:
             contador_palabras[token]=1

    for key,value in contador_palabras.items():
        print(f'{key:<12}{value}')

    print('Número de palabras únicas:',contador_palabras.__len__())

contador_palabras()

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
grades_promedio={}

for key,values in grades.items():
    grades_promedio[key]=sum(values)/len(values)
print(grades_promedio)
#--------------------------------------------------------------------sets------------------------------------------------------------
string= 'wabbawabba'
print(list(string))
print(set(list(string)))

colors={'azul','verde','naranjado','café'};print(colors)

for colores in colors:
    print(colores.upper(),end=' ')
#Se puede crear conjuntos haciendo uso del método nativo set()
#Para crear un set vacio es necesario iniciarlo de la siguiente manera set(). {} se usa para generar diccionarios vacios
#Se puede hacer uso del método issubset() para determinar si un set es igual o esta contenido dentro de otro set.
#Se puede hacer uso del método issuperset() para determinar si un set es igual o contiene a otro


#+++++++++++++++++++++++++++++++++++++++ OPERACIONES MATEMATICAS SOBRE CONJUNTOS++++++++++++++++++++++++++++++++++

set1={1,2,3,4,5};set2={1,4,5,7,8,9,10}
print(set1|set2)  #immprime la union de los dos conjuntos
print(set1&set2) #Imprime la intersección de dos conjuntos
set1|=set2
print(set1)
set2.discard(10)
print(set2)
